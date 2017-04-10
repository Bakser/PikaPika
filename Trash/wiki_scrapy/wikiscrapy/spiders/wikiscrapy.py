import scrapy
import urllib.parse
import json
import re
import langconv

class WikiSpider(scrapy.Spider):
    name = "WikiSpider"
    allowed_domains = ["https://zh.wikipedia.org"]
    start_urls = []

    def start_requests(self):
        API_URL = "https://zh.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvprop=content&titles=%s"
        with open('input.txt','r') as f:
            for w in f.readlines():
                w = w.strip()
                self.start_urls.append(API_URL%w)
        print(self.start_urls)
        for w in self.start_urls:
            yield self.make_requests_from_url(w)

    def parse(self, response):
        filename = "data/" + urllib.parse.unquote(response.url.split("=")[-1]) + '.html'
        with open(filename, 'w') as f:
            text = response.body.decode('utf-8')
            print(text)
            f.write(langconv.Converter('zh-hans').convert(text))
            '''
            keys = re.findall(r'\[\[(\S*?)\]\]',text)
            print(keys)
            keys = [",".join(w.split("|")) for w in keys]
            print(",".join(keys))
            f.write(langconv.Converter('zh-hans').convert(",".join(keys)))
            '''
