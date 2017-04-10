import scrapy
from scrapy.crawler import CrawlerProcess
from wikiscrapy.spiders.wikispider import WikiSpider
from scrapy.settings import Settings

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(WikiSpider(search='三大炮'))
t = process.start() # the script will block here until the crawling is finished
print(dir(process.crawlers))
print("Okay...")
