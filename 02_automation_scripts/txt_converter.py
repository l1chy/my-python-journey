# Developed this script to automate converting legacy 2024 game scripts 
# in the '01_beginner_games' folder from .txt format (yes, I had it all in .txt files lol) to .py format.
import os
from pathlib import Path


def convert_txt_to_py(directory_path="."):
    """Scans the specified directory and renames all .

    txt files to .py files.
    """
    # Convert string path to a Path object (defaults to current directory ".")
    target_dir = Path(directory_path)

    print(f"Scanning directory: {target_dir.resolve()}\n" + "=" * 50)

    # Counter to keep track of changes
    converted_count = 0

    # Iterate through all files in the directory
    for file_path in target_dir.iterdir():
        # Check if it's a file and has a .txt extension
        if file_path.is_file() and file_path.suffix.lower() == ".txt":
            # Create the new filename with .py extension
            new_file_path = file_path.with_suffix(".py")

            # SAFETY CHECK: Don't overwrite an existing .py file with the same name
            if new_file_path.exists():
                print(
                    f"[SKIPPED] Cannot convert '{file_path.name}' -> '{new_file_path.name}' already exists!"
                )
                continue

            try:
                # Rename the file
                file_path.rename(new_file_path)
                print(f"[SUCCESS] Renamed: {file_path.name} -> {new_file_path.name}")
                converted_count += 1
            except Exception as e:
                print(f"[ERROR] Could not rename {file_path.name}. Reason: {e}")

    print("=" * 50)
    print(f"Process complete. Total files converted: {converted_count}")


if __name__ == "__main__":
    # Runs in the current folder where this script is saved
    convert_txt_to_py()