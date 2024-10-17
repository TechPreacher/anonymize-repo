import os


def list_subfolders(base_path) -> list[str]:
    subfolders = []
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and not str(item).startswith("."):
            subfolders.append(item)
    return subfolders


if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    subfolder_list = list_subfolders(current_directory)
    print("Subfolders (excluding .venv):")
    for folder in subfolder_list:
        print(f"- {folder}")
