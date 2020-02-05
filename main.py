#import flask, connect main to templates
from flask import Flask, render_template
#create new flask app object
app = Flask(__name__)

#controler
@app.route("/")#at which url the handler can be reached
def index():
    return render_template("index.html")

@app.route("/abouturl")
def about():
    return render_template("about.html")

@app.route("/portfoliourl")
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run()