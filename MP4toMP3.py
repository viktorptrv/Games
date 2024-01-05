import os
import shutil
from pytube import YouTube


def url_to_mp3(video_url: str):
    video_file = YouTube(video_url).streams.filter().get_audio_only()
    video_file.download()
    mp4_name = video_file.default_filename
    mp3_name = mp4_name.replace('.mp4', '.mp3')
    os.rename(mp4_name, mp3_name)
    shutil.move(mp3_name, "Audio")


def main():
    try:
        input_url = input("Input URL:")
        url_to_mp3(video_url=input_url)
        print("Finished downloading!")
    except Exception as ex:
        print(f"Error: {ex}")

main()