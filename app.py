from flask import Flask

app = Flask(__name__)
#app is the object of the class Flask __name__ is the name of the file


@app.route("/")
#this is a decorator - when this url is requested what shld be returned - "/"empty route
def hello_world():
  return "<p>Hello, Nayan!</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True) #host is set to 0 that to run locally
