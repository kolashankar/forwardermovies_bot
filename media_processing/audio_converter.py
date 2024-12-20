from pydub import AudioSegment
import io

class AudioConverter:
    @staticmethod
    def convert_audio(audio_data, from_format, to_format):
        audio = AudioSegment.from_file(io.BytesIO(audio_data), format=from_format)
        output = io.BytesIO()
        audio.export(output, format=to_format)
        output.seek(0)
        return output.getvalue()

    @staticmethod
    def change_volume(audio_data, from_format, volume_change):
        audio = AudioSegment.from_file(io.BytesIO(audio_data), format=from_format)
        adjusted_audio = audio + volume_change
        output = io.BytesIO()
        adjusted_audio.export(output, format=from_format)
        output.seek(0)
        return output.getvalue()

