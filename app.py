from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
#app is the object of the class Flask __name__ is the name of the file


@app.route("/")
#this is a decorator - when this url is requested what shld be returned - "/"empty route
def hello_world():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  #host is set to 0 that to run locally
