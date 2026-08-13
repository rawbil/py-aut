from pytube import YouTube
from yt_dlp import YoutubeDL
from sys import argv
from dotenv import load_dotenv
import os

load_dotenv()

dir = os.getenv("PATH")


link = argv[1]

# yt = YouTube(link)

# print("Title: ", yt.title)
# print("Views: ", yt.views)

options = {
    "outtmpl": f"{dir}/%(title)s.%(ext)s"
}

with YoutubeDL(options) as ydl:
    info = ydl.extract_info(link, download=True)

print("Title: ", info["title"])
print("Views: ", info["view_count"])
