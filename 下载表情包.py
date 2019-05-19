import requests
from lxml import etree
import os
import urllib.request
# from urllib import request
import re



def parse_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get("alt")
        alt = re.sub(r'[\\\/\:\*\?\"\<\>\|]', '', alt)
        suffix = os.path.splitext(img_url)[1]
        filename = str(x) + alt + suffix
        print(filename+'  下载完成  ')
        urllib.request.urlretrieve(img_url, 'doutu/' +filename)

def main():
    global x
    for x in range(1, 10):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        parse_page(url)


if __name__ == '__main__':
    main()