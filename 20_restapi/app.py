#2 Whites & a Gray: Nada Hameed, Gitae Park, Brianna Tieu
#Softdev
#K12 -- Take and Give
#2022-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
import urllib.request, json
import os

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET','POST'])
def disp_image():
    url = "https://api.nasa.gov/planetary/apod?api_key={}" .format(os.environ.get("TMDB_API_KEY"))
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("main.html", picture = dict["url"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
