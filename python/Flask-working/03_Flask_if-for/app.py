from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def example():
    clarusway = "You are getting better with Clarusway"
    return render_template("index.html", message = False, developer_name = "Serdar")

if __name__ == "__main__":
    app.run(debug = True)