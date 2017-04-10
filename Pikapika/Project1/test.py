# -*- coding:utf-8 -*- 
import urllib2
import urllib
import re
import time
import random
import threading

result = []

def generate_ip_list():
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' }
    req = urllib2.Request(url='http://www.xicidaili.com/nn/',headers = headers)
    res = urllib2.urlopen(req)
    data = res.read()
    foo = re.findall(r'<td>(\d*\.\d*\.\d*\.\d*)</td>\s*<td>(\d*)</td>',data);
    ip_list = []
    for i in foo:
        ip_list.append(i[0]+':'+i[1])
    return ip_list

def check_ip_list(ip_list,url = "http://ip.chinaz.com/getip.aspx"):
    proxys = []
    for w in ip_list:
        proxy_host = "http://"+w
        proxy = {"http":proxy_host}
        print "Checking proxy %s ..."%str(proxy)
        try:
            res = urllib.urlopen(url,proxies=proxy).read()
            fout = open('check_result.txt','w')
            fout.write(res)
            fout.close()
            if (len(res)<1000):
                print "Unavailable!"
            else:
                print "Success!"
                result.append(proxy)
        except Exception,e:
            print "Wrong!" + str(proxy)
            print e


if __name__ == '__main__':
    ip_list = generate_ip_list()
    url = 'http://www.baidu.com'
    #check_ip_list(ip_list,url)
    threads = []
    t1 = threading.Thread(target=check_ip_list,args=(ip_list[0:len(ip_list)/2],url,))
    threads.append(t1)
    t2 = threading.Thread(target=check_ip_list,args=(ip_list[len(ip_list)/2:-1],url,))
    threads.append(t2)
    for t in threads:
        t.setDaemon(False)
        t.start()
    print "All over..."
