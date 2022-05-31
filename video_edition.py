from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import os


def convert_mp4_to_wav(file, output_name):
    sound = AudioSegment.from_file(file)
    sound.export(f'{output_name}.wav', format="wav")
    os.remove(file)


def split_videos_to_smaller_parts_to_mp3(video, start_time, end_time, output_name):
    ffmpeg_extract_subclip(video, start_time, end_time, targetname = output_name)
    convert_mp4_to_wav(output_name, output_name[0:-4])


def get_length_of_video(video):
    clip = VideoFileClip(video)
    return clip.duration


def video_to_shorter(video):
    length = get_length_of_video(video)
    video_duration = 5
    start, end, num = -video_duration, 0, 0
    while length != 0:
        if length < video_duration:
            start += length
            end += length
            length = 0
        else:
            start += video_duration
            end += video_duration
            length -= video_duration
        split_videos_to_smaller_parts_to_mp3(video, start, end, f'videos\\temp{num}.mp4')
        num += 1
