import requests
from lxml import etree



#1.获取数据
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer":"https://movie.douban.com/"
           }
url = "https://movie.douban.com/cinema/nowplaying/xinxiang/"

response = requests.get(url, headers=headers)
text = response.text


#2.提取数据
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    actors= li.xpath("@data-actors")[0]
    region = li.xpath("@data-region")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        'title' : title,
        'score' : score,
        'duration' : duration,
        'actors' : actors,
        'region' : region,
        'thumbnail' : thumbnail
    }
    movies.append(movie)

print(movies)