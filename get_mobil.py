from pytube import YouTube
import os
import pyrebase


def main(linki):
    #link = input("Link: ")
    #directory = input("Directory: ")
    #link = "https://www.youtube.com/watch?v=Ab5g3Ug7ysM"
    link = linki
    print("link girildi")

    try:
        yt = YouTube(link)
        print("try catch")
    except:
        print("Invalid link")
        exit()

    mpt = yt.streams.filter(only_audio=True).first()

    print("convert")
    config = {
        "apiKey": "AIzaSyBkALe1CYOOfQyLNa7Q2odd0P6LZ91jxrA",
        "authDomain": "ytmp3-f6bcc.firebaseapp.com",
        "projectId": "ytmp3-f6bcc",
        "storageBucket": "ytmp3-f6bcc.appspot.com",
        "messagingSenderId": "5264877193",
        "appId": "1:5264877193:web:a59238198e3e2498e94858",
        "measurementId": "G-ZBX5927KVR",
        "serviceAccount": "serviceAccount.json",
        "databaseURL": "https://ytmp3-f6bcc-default-rtdb.firebaseio.com/"
    }
    print("configi geçti")
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    # upload
    # storage.child("s.mp3").put("/audio/MySong.mp3")
    # storage.child("gs_up.jpg").put("/static/images/gs.jpg")

    output = mpt.download(filename='get_v_flask2.mp3')

    print("storage a geldi")

    storage.child("get_mobil.mp3").put("get_v_mobil1.mp3")

    print("storage bitti")



def conv():
    print("Downloading... converter")
    return "return"
