import requests


class MongoLoaderClient:

    def __init__(self, mongo_loader_uri):
        self.mongo_loader_uri = mongo_loader_uri

    def send_to_mongo_loader(self, image_id, bin_file):
        tuple_data = (image_id, bin_file)
        try:
            response = requests.post(self.mongo_loader_uri, files= {"file": tuple_data})
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(str(e))