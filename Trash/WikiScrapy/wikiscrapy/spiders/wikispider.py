import scrapy
import urllib.parse
import json
import re
import langconv
from wikiscrapy.items import WikiScrapyItem

class WikiSpider(scrapy.Spider):
    name = "WikiSpider"
    allowed_domains = ["https://zh.wikipedia.org"]
    start_urls = []
    def __init__(self,filename=None,firsturl=None,search=None,return_type="word"):
        API_URL = "https://zh.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvprop=content&titles=%s"
        if (firsturl != None):
            self.start_urls.append(firsturl)
        if (search != None):
            self.start_urls.append(API_URL%search)
        if (filename != None):
            with open(filename,'r') as f:
                for w in f.readlines():
                    w = w.strip()
                    self.start_urls.append(API_URL%w)

    def start_requests(self):
        API_URL = "https://zh.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvprop=content&titles=%s"
        for w in self.start_urls:
            yield self.make_requests_from_url(w)

    def parse(self, response):
        #print(response.url)
        search = urllib.parse.unquote(response.url.split("=")[-1]) 
        text = response.body.decode('utf-8')
        #print(text)
        res = re.findall(r'#REDIRECT\[\[(\S*)\]\]',text)
        API_URL = "https://zh.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvprop=content&titles=%s"
        if (len(res) != 0):
            print("Redirected to ",res[0])
            return scrapy.Request(API_URL%res[0],callback=self.parse)
        item = WikiScrapyItem()
        item['search'] = search
        item['text'] = langconv.Converter('zh-hans').convert(text)
        with open('data/ans.txt','a') as f:
            sss = json.dumps({'search':search,
                'text':langconv.Converter('zh-hans').convert(text)
                },ensure_ascii=False)
            f.write(sss+'\n')
        yield item
        '''
        f.write(langconv.Converter('zh-hans').convert(text))
        keys = re.findall(r'\[\[(\S*?)\]\]',text)
        print(keys)
        keys = [",".join(w.split("|")) for w in keys]
        print(",".join(keys))
        f.write(langconv.Converter('zh-hans').convert(",".join(keys)))
        '''
