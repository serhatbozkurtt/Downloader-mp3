from pytube import YouTube
import os

def main():
    link = input("Link: ")
    directory = input("Directory: ")

    try:
        yt = YouTube(link)
    except:
        print("Invalid link")
        exit()

    mp3 = yt.streams.filter(only_audio=True).first()

    print("Downloading...")

    output = mp3.download(output_path='C:/Users/Serhat/Programming/PycharmProjects/mp3_db/venv/Include/audio', filename='MySong')

    base, ext = os.path.splitext(output)
    to_mp3 = base + ".mp3"
    os.rename(output, to_mp3)

    print("Download complete")


def convv():
    print("Downloading... converter")
    return "return"
