from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html")

@app.route("/serdar")
def number():
    sayi1, sayi2 = 23 , 45 
    return render_template("body.html", sayi3 = sayi1+sayi2, sayi1 = sayi1, sayi2 = sayi2) # Burada       sayıların ayrıca render template içersinde html file a gönderilirken belirtilmesi gerektiğini vurgula

if __name__ == "__main__":
    app.run(debug = True)