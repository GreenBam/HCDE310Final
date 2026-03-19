import urllib.parse, urllib.request, urllib.error, json
import random as rd

from keys import vkey

args_VC = {"key": vkey, "include": "current"}
base_url_VC = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

args_M = {"hasImages": "true", "q": ""}
base_url_M = "https://collectionapi.metmuseum.org/public/collection/v1/"

#first + second part of assignment, takes in location
def safe_get(location):
    url = base_url_VC + location + "/today?" + urllib.parse.urlencode(args_VC)
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()
    except urllib.error.HTTPError as e:
        print('Error retrieving data: HTTP Error, Error code: ', e.code)
        return None
    except urllib.error.URLError as e:
        print('Failed to reach server, URL error. Reason: ', e.reason)
        return None
    return(json.loads(data))

def safe_get_art(con):
    condition = con['currentConditions']['conditions'].split(" ")
    args_M["q"] = condition[len(condition) - 1]
    url = base_url_M + "/search?" + urllib.parse.urlencode(args_M)
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()
    except urllib.error.HTTPError as e:
        print('Error retrieving data: HTTP Error, Error code: ', e.code)
        return None
    except urllib.error.URLError as e:
        print('Failed to reach server, URL error. Reason: ', e.reason)
        return None
    return (json.loads(data))

def safe_get_ranArt(con):
    artworks = safe_get_art(con)
    if artworks != None:
        objectNum = rd.randint(0, len(artworks["objectIDs"]) - 1)
        url = base_url_M + "/objects/" + str(artworks["objectIDs"][objectNum])
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read().decode()
        except urllib.error.HTTPError as e:
            print('Error retrieving data: HTTP Error, Error code: ', e.code)
            return None
        except urllib.error.URLError as e:
            print('Failed to reach server, URL error. Reason: ', e.reason)
            return None
        return json.loads(data)
    else:
        return None