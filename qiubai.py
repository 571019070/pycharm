import requests

from lxml import etree


class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/hot/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1,14)]


    def parse_url(self,url):
        response = requests.get(url, headers = self.headers)
        return response.content.decode()


    def get_content_list(self,html_str):#提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            item = {}
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = [i.replace("\n", "") for i in item["content"]]
            item["authon_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
            item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
            item["content_img"] = "https:"+item["content_img"][0] if len(item["content_img"])>0 else None
            item["touxiang_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
            item["touxiang_img"] = "https:"+item["touxiang_img"][0] if len(item["touxiang_img"])>0 else None
            content_list.append(item)
        return content_list


    def save_content_list(self,content_list):
        for i in content_list:
            print(i)



    def run(self):
        # 1.start_url
        url_list = self.get_url_list()
        # 2.遍历， 发送请求获取响应
        for url in url_list:
            html_str = self.parse_url(url)
        # 3.提取数据
        content_list =self.get_content_list(html_str)
        # 4.保存
        self.save_content_list(content_list)




if __name__ == '__main__':
    qiubai = QiubaiSpider()
    qiubai.run()