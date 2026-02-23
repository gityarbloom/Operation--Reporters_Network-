from model_mongo_loader_sending import MongoLoaderClient
from model_metadata_extractor import MetadataExtractor
from model_Ingestion_config import IngestionConfig
from model_kafka_publisher import KafkaPublisher
from model_ocr_ngine import OCREngine
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
    


pathsss = IngestionConfig()
mongo_loader_sending = MongoLoaderClient()
m_data_extractor = MetadataExtractor()


ocr_uri = str(pathsss.ocr_uri)
folder_path = str(pathsss.folder_path)
kafka_config = pathsss.kafka_config
mdb_loader_uri = str(pathsss.mongo_loader_uri)

kafka_producer = KafkaPublisher(kafka_config)