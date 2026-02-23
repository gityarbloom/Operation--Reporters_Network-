import requests


class OCREngine:

    @staticmethod
    def extract_text(ocr_uri, image_path):
        with open(image_path, "rb") as f:
            response = requests.post(ocr_uri, files={"file": f})
        return response.json()