import os
from pathlib import Path


# ============================================================
# Utility Functions
# ============================================================

def create_folder(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def download_images():
    pass


def download_labels():
    pass


# ============================================================
# Main Function
# ============================================================

def main():
    download_images()
    download_labels()


# ============================================================
# Entry Point - Run main only when executed directly
# ============================================================

if __name__ == '__main__':
    main()