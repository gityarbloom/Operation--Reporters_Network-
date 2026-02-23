from model_mongo_loader_sending import MongoLoaderClient
from utils import get_all_files_path, read_to_binary
from model_Ingestion_config import IngestionConfig
from model_ocr_ngine import OCREngine
import json



# ocr_uri = str(pathsss.ocr_uri)
# kafka_config = str(pathsss.kafka_config)
pathsss = IngestionConfig()
mongo_loader_sending = MongoLoaderClient()



images_path_list = get_all_files_path(str(pathsss.folder_path))

for i in range(len(images_path_list)):
    bin_file = read_to_binary(images_path_list[i])
    mongo_loader_sending.send_to_mongo_loader_service(str(pathsss.mongo_loader_uri), bin_file)



# def read_from_photos_folder(file_path: str):
#     metadata = extract_metadata(str(file_path))
#     binary_data = read_to_binary(str(file_path))
#     photos_metadata = {"id": file_path, "metadata": metadata, "binary": binary_data}
#     return photos_metadata