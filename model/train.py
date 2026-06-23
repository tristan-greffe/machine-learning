import argparse
import shutil
import sys
from pathlib import Path
from ultralytics import YOLO


# ============================================================
# Paths
# ============================================================

# train.py lives at geo-ml/model/train.py → parents[1] = geo-ml/
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR  = PROJECT_ROOT / "model" / "dataset"
WEIGHTS_DIR  = PROJECT_ROOT / "model" / "weights"
FRONTEND_DIR = PROJECT_ROOT / "frontend" / "public" / "models"
RUNS_DIR     = PROJECT_ROOT / "model" / "runs"


# ============================================================
# Training defaults
# ============================================================

# Must match WINDOW_SIZE in model/dataset/utils.py
IMAGE_SIZE       = 640
DEFAULT_EPOCHS   = 80
DEFAULT_BATCH    = 16
DEFAULT_PATIENCE = 20
# Nano checkpoint — smallest footprint, fastest to converge
DEFAULT_BASE     = "yolov8n.pt"


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Train a YOLO model on a dataset built by model/dataset/main.py"
    )
    parser.add_argument("--model",     required=True, choices=["buildings", "pools"],
                        help="Which dataset to train on")
    parser.add_argument("--epochs",    type=int, default=DEFAULT_EPOCHS)
    parser.add_argument("--batch",     type=int, default=DEFAULT_BATCH)
    parser.add_argument("--patience",  type=int, default=DEFAULT_PATIENCE,
                        help="Early-stop patience (epochs with no mAP improvement)")
    parser.add_argument("--base",      default=DEFAULT_BASE,
                        help="Pretrained checkpoint to fine-tune from")
    parser.add_argument("--resume",    action="store_true",
                        help="Resume training from model/runs/<model>/weights/last.pt")
    parser.add_argument("--no-export", action="store_true",
                        help="Skip ONNX export after training")
    args = parser.parse_args()

    data_yaml = DATASET_DIR / args.model / "dataset.yaml"
    if not data_yaml.exists():
        print(f"Dataset not found: {data_yaml}")
        print(f"  → run: python -m model.dataset.main --{args.model}")
        sys.exit(1)

    WEIGHTS_DIR.mkdir(parents=True, exist_ok=True)
    FRONTEND_DIR.mkdir(parents=True, exist_ok=True)

    # --- Train ---
    if args.resume:
        last_checkpoint = RUNS_DIR / args.model / "weights" / "last.pt"
        if not last_checkpoint.exists():
            print(f"No checkpoint to resume from: {last_checkpoint}")
            sys.exit(1)
        print(f"Resuming from {last_checkpoint}")
        model = YOLO(str(last_checkpoint))
        model.train(resume=True)
    else:
        model = YOLO(args.base)
        model.train(
            data=str(data_yaml),
            epochs=args.epochs,
            imgsz=IMAGE_SIZE,
            batch=args.batch,
            patience=args.patience,
            project=str(RUNS_DIR),
            name=args.model,
            exist_ok=True,
            # Aerial imagery has no canonical orientation — full rotation and both flips are valid
            fliplr=0.5,
            flipud=0.5,
            degrees=180,
            # Mild colour jitter to handle IGN sensor variability across acquisition zones
            hsv_h=0.015,
            hsv_s=0.5,
            hsv_v=0.4,
            mosaic=1.0,
            verbose=True,
        )

    best_checkpoint = RUNS_DIR / args.model / "weights" / "best.pt"
    destination_pt  = WEIGHTS_DIR / f"{args.model}.pt"
    shutil.copy(best_checkpoint, destination_pt)
    print(f"\nWeights → {destination_pt}")

    # --- Export ONNX for in-browser inference ---
    if args.no_export:
        return

    best_model       = YOLO(str(best_checkpoint))
    onnx_path        = best_model.export(
        format="onnx",
        imgsz=IMAGE_SIZE,
        opset=12,
        simplify=True,
        nms=False,      # NMS is handled in JS by the frontend (onnxruntime-web)
        dynamic=False,  # fixed input shape required by onnxruntime-web
    )
    destination_onnx = FRONTEND_DIR / f"{args.model}.onnx"
    shutil.copy(onnx_path, destination_onnx)
    size_mb = destination_onnx.stat().st_size / 1024 / 1024
    print(f"ONNX → {destination_onnx}  ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
