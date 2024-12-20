from PIL import Image, ImageDraw, ImageFont
import io

class WatermarkService:
    @staticmethod
    def add_watermark(photo, watermark_text):
        # Open the image
        image = Image.open(io.BytesIO(photo.file.read()))
        
        # Create a drawing object
        draw = ImageDraw.Draw(image)
        
        # Choose a font and size
        font = ImageFont.truetype("arial.ttf", 36)
        
        # Get image size
        width, height = image.size
        
        # Calculate text size
        text_width, text_height = draw.textsize(watermark_text, font)
        
        # Calculate text position (bottom right corner)
        x = width - text_width - 10
        y = height - text_height - 10
        
        # Add text to image
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
        
        # Save the watermarked image to a bytes buffer
        buffer = io.BytesIO()
        image.save(buffer, format='JPEG')
        buffer.seek(0)
        
        return buffer

    @staticmethod
    def remove_watermark(photo):
        # This is a placeholder. Removing watermarks is a complex task and often not perfect.
        # For now, we'll just return the original photo
        return photo

    @staticmethod
    def update_watermark_settings(user, watermark_text, position, font, color, opacity):
        # Update user's watermark settings in the database
        user.watermark_text = watermark_text
        user.watermark_position = position
        user.watermark_position = position
        user.watermark_font = font
        user.watermark_color = color
        user.watermark_opacity = opacity
        user.save()

    @staticmethod
    def get_watermark_settings(user):
        return {
            'text': user.watermark_text,
            'position': user.watermark_position,
            'font': user.watermark_font,
            'color': user.watermark_color,
            'opacity': user.watermark_opacity
        }

