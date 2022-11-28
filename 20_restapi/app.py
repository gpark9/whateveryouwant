<<<<<<< HEAD
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
=======
#Pateo Furniture Gitae Park, Vivian Teo
#Softdev
# K20 A RESTful Journey
#2022-11-21

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET','POST']) 
def disp_image():
    # read in key from txt file
    file = open("key_nasa.txt", 'r')
    key = file.read()
    file.close()
    # print(key)

    url = 'https://api.nasa.gov/planetary/apod'

    # dict for query
    key_value = {'api_key':key}

    # get the content from the url
    response = requests.get(url, params=key_value)
    print(response.url)

    # turn the content into json object
    json = response.json()
    print(json)

    # read in the values for these specific keys to access image, title, and explanation
    explanation = json["explanation"]
    img_url = json["hdurl"]
    title = json["title"]

    # print(explanation)
    # print(img_url)
    # print(title)

    return render_template( 'main.html', img=img_url, title=title, explanation=explanation )

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
>>>>>>> d22c1a734d96e3d47b743c1392fb0262cc5de355
