import scrapy
import scrapy.log
from scrapy.crawler import CrawlerProcess
from wikiscrapy.spiders.wikispider import WikiSpider
from scrapy.settings import Settings

process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

def do_scrapy(lstA,lstB):
    print(dir(scrapy.log.logger))
    scrapy.log.start(logfile=None, loglevel=scapy.log.CRITICAL, logstdout=None)
    with open('data/input.txt','w') as fout:
        fout.write("\n".join(lstA));
        process.crawl(WikiSpider(filename = 'data/input.txt'))
        t = process.start()

    with open('data/output.txt','r') as fin:
        fin.read();

if __name__ == '__main__':
    do_scrapy(['欧洲','亚洲'],[])
