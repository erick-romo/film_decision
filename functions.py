import urllib2
import json

#Returns movies based off director
def offDirector(director):
    
    f = urllib2.urlopen("http://netflixroulette.net/api/api.php?director=" + director.replace(" ", "%20"))
    json_string = f.read()
    directorFile = json.loads(json_string)
    f.close()
    return directorFile

#Returns movies based off director
def offActor(actor):
    
    f = urllib2.urlopen('http://netflixroulette.net/api/api.php?actor=' + actor.replace(" ", "%20"))
    json_string = f.read()
    actorFile = json.loads(json_string)
    f.close()

    return actorFile