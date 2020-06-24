#ToBeatElite
from __future__ import unicode_literals
from validators import url
import youtube_dl
import os

def main(video_link, file_name, output_format):

    if url(video_link.replace(" ", "")) or output_format in [1, 2, 3]:
        
        try:
            desired_file_name = file_name.replace(" ", "_")

            ydl_opts = {
                "fileformat": "bestaudio/best",
                "outtmpl": f"downloaded_videos/{desired_file_name}.webm",
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_link.replace(" ", "")])

            if output_format == 1: os.system(f"ffmpeg -i downloaded_videos/{desired_file_name}.webm downloaded_videos/{desired_file_name}.mp4")
            elif output_format == 2: os.system(f"ffmpeg -i downloaded_videos/{desired_file_name}.webm downloaded_videos/{desired_file_name}.mp4")
            elif output_format == 3: os.system(f"ffmpeg -i downloaded_videos/{desired_file_name}.webm downloaded_videos/{desired_file_name}.mp4")
        
        except: return "An Error Occured\n"

    else: return "Invalid Parameters"
    
def start():

    video_url = input("Youtube Video Downloader V1\nUrl: ")
    file_title = input("Desired File Name : ")
    output_type = input("Output Type: \n1 for mp4\n2 for mp3\n3 for wav\n : ")
    
    main(video_url, file_title, int(output_type))

if __name__ == "__main__":
    while True: start()