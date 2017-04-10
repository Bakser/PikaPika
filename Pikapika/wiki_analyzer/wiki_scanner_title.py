#python3
#coding:utf-8
import xml.sax
import time
import re
import pymysql
import langconv


class WikiHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.content = ''
        self.title = ''
        self.tag = None
        self.count = 0
        self.fout = open('title.txt','w')
        self.connection= pymysql.connect(host='localhost',user='root',db ='wikidb',charset='utf8')
        self.cursor = self.connection.cursor()

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        if (tag == 'title'):
            self.tag = tag

    def __del__(self):
        self.fout.close()
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

    # 元素结束事件处理
    def endElement(self, tag):
        if (self.tag == None):
            self.content = ''
            self.tag = None
            return
        if (self.tag == 'title' and re.search(r':',self.content)):
            self.content = ''
            self.tag = None
            return
        self.content = langconv.Converter('zh-hans').convert(self.content)
        if (self.tag == 'title'):
            self.title_flag = True
            self.content = self.content.lstrip().rstrip()
            self.title = self.content
            self.count += 1
            self.fout.write(self.content+'\n')
            if (self.count%1000==0):
                print(self.count)
            try:
                self.cursor.execute("INSERT INTO main (title) VALUES (%s) ",(self.content))
            except pymysql.err.InternalError as e:
                return
            except pymysql.err.DataError as e:
                return 
        self.tag = None

    # 内容事件处理
    def characters(self, content):
        self.content += content


if ( __name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = WikiHandler()
    parser.setContentHandler( Handler )
    print("Part1...")
    #parser.parse("zhwiki-20161020-pages-meta-current1.xml")
    print("Part2...")
    parser.parse("zhwiki-20161020-pages-meta-current2.xml")
    print("Part3...")
    parser.parse("zhwiki-20161020-pages-meta-current3.xml")
    print("Part4...")
    parser.parse("zhwiki-20161020-pages-meta-current4.xml")
