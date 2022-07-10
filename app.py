from flask import Flask
import convert
import upload
import get
import get_mobil

app = Flask(__name__)

@app.route("/")
def baslangic_ap():
    #convert.conv()
    #upload.main()
    get.main()
    return "Flask Api 3 Denemesi"

@app.route("/mobil")
def get_mobil():
    return "get mobil"

@app.route("/mobilg/<string:link>")
def mobilget(link):
    print("linke geldi")


    return "mobil link: " + link

@app.route("/begmobil/<link>")
def begin_mobil(link):
    print("linke geldi")
    get_mobil.main(link)
    print("fonka gitti")

    return "mobil link: " + link


if __name__ == "__main__":
    app.run()
