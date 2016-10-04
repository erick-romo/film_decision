from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

from NetflixRoulette import *
from livereload import Server
import urllib2
import json

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method=="POST":
        actor = request.form["Actor"]
        director = request.form["Director"]
        return render_template('home.html')
@app.route("/feature")
def movie_info(city_name):
    Title = parsed_json["show_title"]
    Year = parsed_json["release_year"]
    Rating = parsed_json["rating"]
    Cast = parsed_json["show_cast"]
    Director = parsed_json["director"]
    Plot  = parsed_json["summary"]
    Length = parsed_json["runtime"]
    return render_template('feature.html',featTitle= Title, featYear = Year, featRating = Rating, featCast = Cast, featDirector= Director, featPlot = Plot, featLength = Length, )
 
 
Server(app.wsgi_app).serve()
