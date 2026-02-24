from model_ingestion_orchestrator import *

images_path_list = get_all_files_path(folder_path)

for i in range(len(images_path_list)):
    image_id = images_path_list[i]
    bin_txt = read_to_binary(image_id)

    send_to_mongo_loader = mongo_loader_sending.send_to_mongo_loader(bin_txt)
    print(send_to_mongo_loader)

    raw_txt = extract_text(image_id)
    metadata = m_data_extractor.extract_metadata(image_id)
    data = {"image_id": image_id, "raw_txt": raw_txt, "metadata": metadata}    
    send_to_kafka = kafka_producer.send_to_kafka("RAW", data)
    print(send_to_kafka)