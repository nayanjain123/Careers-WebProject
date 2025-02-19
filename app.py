from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
#app is the object of the class Flask __name__ is the name of the file

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'   
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs. 15,00,000'   
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000'   
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'$120,000'
  }
]


@app.route("/")
#this is a decorator - when this url is requested what shld be returned - "/"empty route
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")

@app.route("/api/jobs")#api route of the jobs
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  #host is set to 0 that to run locally
