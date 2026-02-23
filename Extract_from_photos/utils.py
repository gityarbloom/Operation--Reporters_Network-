import os


def get_all_files_path(folder_path: str):
    all_files_path = []
    for f in os.listdir(folder_path):
        if f.endswith('.png'):
            file_path = f"{folder_path}/{f}"
            all_files_path.append(file_path)
    return all_files_path


def read_to_binary(file_path: str):
    with open(file_path, "rb") as f:
        return f.read()