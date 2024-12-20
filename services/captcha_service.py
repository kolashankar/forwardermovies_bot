import cv2
import numpy as np
import pytesseract
from PIL import Image
import io

class CaptchaService:
    @staticmethod
    def solve_captcha(image_data):
        try:
            # Convert image data to OpenCV format
            nparr = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Preprocess the image
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
            
            # Perform text extraction
            text = pytesseract.image_to_string(thresh, config='--psm 7')
            return text.strip()
        except Exception as e:
            print(f"Captcha solving error: {str(e)}")
            return None

    @staticmethod
    def handle_captcha(message):
        if message.photo:
            largest_photo = message.photo[-1]
            file = largest_photo.get_file()
            image_data = file.download_as_bytearray()
            solved_captcha = CaptchaService.solve_captcha(image_data)
            if solved_captcha:
                return solved_captcha
        return None

