from flask import Flask, render_template, request, redirect, session
from flask_bootstrap import Bootstrap 
from NetflixRoulette import *
from functions import *
from livereload import Server
import urllib2
import json
import pprint
from random import randint




app = Flask(__name__)
Bootstrap(app)

if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method=="POST":
        try:
            actor = request.form["Actor"]
            if len(actor) > 1: 
                movieList = offActor(actor)
                movieChoice = randint(0, len(movieList))
                movie = movieList[movieChoice]
                return render_template('feature.html', movie = movie)
        except: 
             return render_template('error.html')
        return render_template('home.html')
@app.route("/feature")
def movie_info(city_name):
    return render_template('feature.html')
 
 
Server(app.wsgi_app).serve()
