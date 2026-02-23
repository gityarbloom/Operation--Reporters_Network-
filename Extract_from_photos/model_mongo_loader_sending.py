import requests


class MongoLoaderClient:

    @staticmethod
    def send_to_mongo_loader(mongo_loader_uri, image_id, bin_file):
        tuple_data = (image_id, bin_file)
        try:
            response = requests.post(mongo_loader_uri, files= {"file": tuple_data})
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(str(e))