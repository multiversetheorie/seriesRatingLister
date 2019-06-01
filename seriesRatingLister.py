import json
import urllib.request
import urllib.parse

seriestitle = input("Insert series title here: ")
apikey = input("Insert OMDB API key: ")

encodedtitle = urllib.parse.quote(seriestitle)

seriesurl = "http://www.omdbapi.com/?t=" + encodedtitle +"&apikey=" + apikey
seriesdata = urllib.request.urlopen(seriesurl).read().decode()

seriesobj = json.loads(seriesdata)

seasoncount = int(seriesobj['totalSeasons'])

seasonslist = []

for r in range(1,seasoncount+1):
    seasonslist.append(r)

for e in range(len(seasonslist)):
    url ="http://www.omdbapi.com/?t=" + encodedtitle + "&Season=" + str(seasonslist[e]) + "&apikey=" + apikey
    data = urllib.request.urlopen(url).read().decode()

    obj = json.loads(data)

    episodes = obj['Episodes']

    for i in range(len(episodes)):
        epdict = episodes[i]
        print(str(seasonslist[e]) + "." + epdict['Episode'] + ": " + epdict['imdbRating'])
