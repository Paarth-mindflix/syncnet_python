import os
import random
from pydub import AudioSegment
import subprocess
import cv2
import numpy as np
import speech_recognition as sr
from yt_dlp import YoutubeDL

# Configuration
DOWNLOAD_DIR = "./youtube_videos"

# Ensure directories exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_video(url, download_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': os.path.join(download_path, '%(id)s.%(ext)s'),
        'noplaylist': True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print("downloaded")
            video_path = ydl.prepare_filename(info)
            return video_path
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

# Main function to build the dataset
def build_dataset():
    # video_count = 0
    with open("D:/Experiments/video_links_Huberman_testing.txt", "r") as file:
        video_urls = file.read().splitlines()

    # video_count = len(video_urls)
    for video_count, url in enumerate(video_urls):

        print(f"Processing video {video_count + 1}: {url}")
        video_path = download_video(url, DOWNLOAD_DIR)


if __name__ == "__main__":
    build_dataset()
