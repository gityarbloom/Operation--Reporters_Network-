from fastapi import HTTPException
import requests


class MongoLoaderClient:

    @staticmethod
    def send_to_mongo_loader_service(mongo_loader_uri, bin_data: bytes):
        try:
            response = requests.post(mongo_loader_uri, data=bin_data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=503, detail=e)
