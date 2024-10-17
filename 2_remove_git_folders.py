import os
import shutil

import helpers


def remove_github_folders(base_path):
    folders_to_check = helpers.list_subfolders(base_path)

    for folder in folders_to_check:
        github_path = os.path.join(base_path, folder, ".github")
        if os.path.exists(github_path):
            try:
                shutil.rmtree(github_path)
                print(f"Removed .github folder from {folder}")
            except Exception as e:
                print(f"Error removing .github folder from {folder}: {e}")
        else:
            print(f"No .github folder found in {folder}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    remove_github_folders(script_dir)
