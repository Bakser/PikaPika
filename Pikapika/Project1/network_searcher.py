# -*- coding:utf-8 -*- 
import urllib2
import re
import cgi
import time
import requests
import random
import httplib
from bs4 import BeautifulSoup


ip_update = -1
ip_list = []

def get_ip_list():
    url = 'http://www.xicidaili.com/nn/';
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    global ip_list
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    print "IP list updated ..."
    print ip_list

def get_random_ip():
    global ip_update
    global ip_list
    if (ip_update < 0):
        get_ip_list()
        ip_update = 100
    else:
        ip_update -= 1
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    return proxy_ip

def open_url(url,enable_proxy=True):
        #ip = get_random_ip()
        ip = '180.76.154.5:8888'
        print url
        print "Process url " + '...' + " with proxy " + ip 
        proxy_handler = urllib2.ProxyHandler({"http" : ip})
        null_proxy_handler = urllib2.ProxyHandler({})
        if enable_proxy:
            opener = urllib2.build_opener(proxy_handler)
        else:
            opener = urllib2.build_opener(null_proxy_handler)
        urllib2.install_opener(opener)
        i_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'}
        req = urllib2.Request(url,headers=i_headers)
        time.sleep(0.5)
        try:
            print "Sleepp....."
            html = urllib2.urlopen(req)
            print "Sleepp....."
            if (not html.geturl() == url):
                print "Warning: URL redirected..."
            return html
        except httplib.BadStatusLine:
            print "ERROR"
            return None
        except urllib2.URLError:
            print "Error: URLERROR"
            return open_url(url,enable_proxy)



if __name__ == '__main__':
    fin = open('keywords_output.txt','r')
    lst = fin.read().split('\n')
    fout = open('keywords_ranking.txt','w')
    lst = lst[0:-2]
    for w in lst:
        res = open_url('https://baike.baidu.com/item/%s'%(w))
        if (res == None):
            fout.write("--\n")
            continue
        text = res.read()
        for ww in lst:
            print ww,len(re.findall(ww,text)),
            fout.write(str(len(re.findall(ww,text)))+'\t')
        fout.write('\n')
        time.sleep(1)
        print ;
