import requests


class MongoLoaderClient:

    def __init__(self, mongo_loader_uri):
        self.mongo_loader_uri = mongo_loader_uri

    def send_to_mongo_loader(self, bin_file):
        try:
            response = requests.post(self.mongo_loader_uri, data=bin_file)
            response.raise_for_status()
            return "\nSuccessfulsending to mongo_loader \n"
        except Exception as e:
            raise Exception(str(e))