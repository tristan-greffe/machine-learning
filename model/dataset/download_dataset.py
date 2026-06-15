import argparse
import sys
from pathlib import Path

# Add the project root (geo-ml/) to the Python path so imports like
# `from model.data.yolo_common import ...` work regardless of where the script is launched from.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


# ============================================================
# Constants / Configuration
# ============================================================

# Output root: datasets are written to model/dataset/buildings/ and model/dataset/pools/
DATASET_DIR = Path(__file__).parent


# ============================================================
# Utility Functions
# ============================================================

def create_folder(path):
    Path(path).mkdir(parents=True, exist_ok=True)


# ============================================================
# Buildings
# ============================================================

def prepare_buildings():
    pass


# ============================================================
# Pools
# ============================================================

def prepare_pools():
    pass


# ============================================================
# Main
# ============================================================

def main():
    # --- Arguments ---
    # description is shown at the top of the --help output
    parser = argparse.ArgumentParser(
        description="Download and prepare YOLO datasets for buildings and/or pools."
    )
    parser.add_argument("--buildings", action="store_true", help="Prepare the buildings dataset")
    parser.add_argument("--pools", action="store_true", help="Prepare the pools dataset")
    args = parser.parse_args()

    # Default: both if no flag is given
    run_buildings = args.buildings or (not args.buildings and not args.pools)
    run_pools     = args.pools     or (not args.buildings and not args.pools)

	# --- Run ---
    if run_buildings:
        print("-- Buildings")
        prepare_buildings()

    if run_pools:
        print("-- Pools")
        prepare_pools()


if __name__ == "__main__":
    main()
