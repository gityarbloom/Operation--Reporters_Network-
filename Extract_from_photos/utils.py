
# def extract_metadata(file_path: str):
#     with Image.open(file_path) as img:
#         metadata = {
#             "width": img.width,
#             "height": img.height,
#             "format": img.format,
#             "file_size_bytes": os.path.getsize(file_path)
#         }
#     return metadata

# def read_to_binary(file_path: str):
#     with open(file_path, "rb") as f:
#         return f.read()

# def get_all_file_paths(folder_path: str):
#     photos_list = []
#     for f in os.listdir(folder_path):
#         if f.endswith('.png'):
#             file_path = f"{folder_path}/{f}"
#             photos_list.append(file_path)
#     return photos_list

# def read_from_photos_folder(file_path: str):
#     metadata = extract_metadata(str(file_path))
#     binary_data = read_to_binary(str(file_path))
#     photos_metadata = {"id": file_path, "metadata": metadata, "binary": binary_data}
#     return photos_metadata
