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
