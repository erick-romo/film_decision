import urllib2
import json
def offDirector(director):
    
    f = urllib2.urlopen("http://netflixroulette.net/api/api.php?director=" + director )
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    daDict = {"Title: ": parsed_json["show_title"], "Release Year: ": parsed_json["release_year"], "Rating: ": parsed_json["rating"], "Cast: ": parsed_json["show_cast"], "Director: ": parsed_json["director"], "Plot Summary: ": parsed_json["summary"], "Length: ": parsed_json["runtime"]}
    daDeets = daDict
    return daDeets
#Returns movies based on a director
http://netflixroulette.net/api/api.php?director=Quentin%20Tarantino
def offActor(actor):
    
    f = urllib2.urlopen("http://netflixroulette.net/api/api.php?actor=" + actor )
    json_string = f.read()
    parsed_json = json.loads(json_string)
    f.close()
    daDict = {"Title: ": parsed_json["show_title"], "Release Year: ": parsed_json["release_year"], "Rating: ": parsed_json["rating"], "Cast: ": parsed_json["show_cast"], "Director: ": parsed_json["director"], "Plot Summary: ": parsed_json["summary"], "Length: ": parsed_json["runtime"]}
    daDeets = daDict
    return daDeets