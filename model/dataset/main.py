import argparse
import sys
from pathlib import Path

# Add the project root (geo-ml/) to sys.path so `from model.dataset.*` works
# regardless of the working directory the script is launched from.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from model.dataset.buildings import prepare_buildings
from model.dataset.pools import prepare_pools

def main():
    # --- Arguments ---
    # description is shown at the top of the --help output
    parser = argparse.ArgumentParser(
        description="Download and prepare YOLO datasets for buildings and/or pools."
    )
    parser.add_argument("--buildings", action="store_true", help="Prepare the buildings dataset")
    parser.add_argument("--pools",     action="store_true", help="Prepare the pools dataset")
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
