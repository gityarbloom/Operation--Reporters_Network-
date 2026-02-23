from dotenv import load_dotenv
from PIL import Image
import requests
import os



load_dotenv()
FOLDER_PATH = os.getenv("PHOTOS_FOLDER_PATH")
OCR_URI = os.getenv("OCR_URI")

def send_image_to_ocr(image_path: str):
    with open(image_path, "rb") as f:
        response = requests.post(OCR_URI, files={"file": f})
    return response.json()