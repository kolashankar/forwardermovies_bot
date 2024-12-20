import pypandoc
import io

class FileConverter:
    @staticmethod
    def convert_document(file_data, from_format, to_format):
        input_file = io.BytesIO(file_data)
        output = pypandoc.convert_file(input_file, to_format, format=from_format)
        return output.encode('utf-8')

    @staticmethod
    def supported_formats():
        return pypandoc.get_pandoc_formats()

