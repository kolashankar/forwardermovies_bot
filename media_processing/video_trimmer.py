from moviepy.editor import VideoFileClip
import io

class VideoTrimmer:
    @staticmethod
    def trim_video(video_data, start_time, end_time):
        with VideoFileClip(io.BytesIO(video_data)) as video:
            trimmed_video = video.subclip(start_time, end_time)
            output = io.BytesIO()
            trimmed_video.write_videofile(output, codec="libx264", audio_codec="aac")
            output.seek(0)
            return output.getvalue()

    @staticmethod
    def get_video_duration(video_data):
        with VideoFileClip(io.BytesIO(video_data)) as video:
            return video.duration

