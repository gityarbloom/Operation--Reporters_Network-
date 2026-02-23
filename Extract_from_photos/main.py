from utils import *
import json


images_path_list = get_all_files_path(folder_path)

for i in range(len(images_path_list)):
    image_id = images_path_list[i]
    raw_txt = read_to_binary(image_id)
    metadata = m_data_extractor.extract_metadata(image_id)

    mongo_loader_sending.send_to_mongo_loader(mdb_loader_uri, image_id, raw_txt)

    value = {"image_id": image_id, "raw_txt": raw_txt.decode("utf-8"), "metadata": metadata}    
    kafka_producer.send_to_kafka("RAW", value)