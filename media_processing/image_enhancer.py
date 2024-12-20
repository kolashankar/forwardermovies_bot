from PIL import Image, ImageEnhance
import io

class ImageEnhancer:
    @staticmethod
    def enhance_image(image_data, brightness=1.0, contrast=1.0, color=1.0, sharpness=1.0):
        image = Image.open(io.BytesIO(image_data))
        
        enhancers = [
            (ImageEnhance.Brightness, brightness),
            (ImageEnhance.Contrast, contrast),
            (ImageEnhance.Color, color),
            (ImageEnhance.Sharpness, sharpness)
        ]
        
        for enhancer_class, factor in enhancers:
            enhancer = enhancer_class(image)
            image = enhancer.enhance(factor)
        
        output = io.BytesIO()
        image.save(output, format='JPEG')
        output.seek(0)
        return output.getvalue()

