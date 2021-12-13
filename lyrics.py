import requests, urllib
from bs4 import BeautifulSoup

def searchLyrics(query):
        with requests.session() as web:
            web.headers["user-agent"] = "Mozilla/5.0"
            url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
            data = BeautifulSoup(url.content, "html5lib")
            result = []
            for trackList in data.findAll("ul", {"class":"tracks list"}):
                imgalt = ""
                for x in trackList.findAll("img"):
                    img = x['srcset'].split(' 320w, ')
                    imgalt += img[0]
                for urlList in trackList.findAll("a"):
                    artist = ""
                    if 'artist' in urlList["class"]:
                        artist += urlList.text
                    if 'lyrics' in urlList["href"]:
                        title = urlList.text
                        url = urlList["href"]
                    result.append({"title": title, "artist": artist.title(), "url": url, "img": imgalt})
            data = result[1]
            lyric = ""
            with requests.session() as web:
                web.headers["user-agent"] = "Mozilla/5.0"
                url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data['url'])))
                data1 = BeautifulSoup(url.content, "html5lib")
                x = data1.findAll("p", {"class": "mxm-lyrics__content"})
                #print(x)
                if len(x) == 2:
                    try:
                        lyric += x[0].text + "\n" + x[1].text
                    except:
                        lyric += x[0].text
                if len(x) == 1:
                    lyric += x[0].text
            data['lyrics'] = lyric
            return data
