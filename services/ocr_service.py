import pytesseract
from PIL import Image
import io

class OCRService:
    @staticmethod
    def extract_text_from_image(image_data):
        try:
            image = Image.open(io.BytesIO(image_data))
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            print(f"OCR error: {str(e)}")
            return None

    @staticmethod
    def process_message_with_ocr(message):
        if message.photo:
            largest_photo = message.photo[-1]
            file = largest_photo.get_file()
            image_data = file.download_as_bytearray()
            extracted_text = OCRService.extract_text_from_image(image_data)
            if extracted_text:
                message.ocr_text = extracted_text
        return message

