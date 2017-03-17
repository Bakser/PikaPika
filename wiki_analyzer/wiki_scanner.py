#coding:utf-8
import xml.sax
import time
import re
import pymysql
import langconv


class WikiHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.content = ''
        self.title = ''
        self.tag = None
        self.accept = ['title','text']
        self.title_flag = False
        #self.fout = open('result.txt','w')
        self.pattern = re.compile(':')
        self.connection= pymysql.connect( host='localhost', user='root', db ='wikidb',charset='utf8')
        self.cursor = self.connection.cursor()
        self.sqlpattern = 'INSERT INTO main VALUES (%s,%s)'
        self.count = 0

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        if (tag in self.accept):
            self.tag = tag

    # 元素结束事件处理
    def endElement(self, tag):
        if (self.tag == None):
            self.content = ''
            self.tag = None
            return
        if (self.tag == 'title' and re.search(self.pattern,self.content)):
            self.content = ''
            self.tag = None
            return
        if (self.tag == 'text' and not self.title_flag):
            self.content = ''
            self.tag = None
            return
        self.content = langconv.Converter('zh-hans').convert(self.content)
        if (self.tag == 'title'):
            self.title_flag = True
            self.content = self.content.lstrip().rstrip()
            #self.fout.write('<title>'+self.content+'</title>\n')
            self.title = self.content
        if (self.tag == 'text'):
            self.title_flag = False
            self.text = self.content
            print(self.title,len(self.text))
            #print('<text>'+self.content+'</text>\n')
            self.text=self.text.encode('utf-8',errors='strict')
            '''
            try:
                self.cursor.execute(self.sqlpattern,(self.title,self.text))
            except pymysql.err.InternalError as e:
                print("Bad coding..."+self.title)
                try:
                    self.cursor.execute(self.sqlpattern,(self.title,"..."))
                except pymysql.err.InternalError as e:
                    print("Title Bad coding...")

            self.count += 1
            if (self.count % 100 == 0):
                print(str(self.count)+'...')
            '''
        #print self.content
        self.content = ''
        self.tag = None

    # 内容事件处理
    def characters(self, content):
        self.content += content

    def __del__(self):
        #self.fout.close()
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

if ( __name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = WikiHandler()
    parser.setContentHandler( Handler )
 #   print("Part1...")
 #   parser.parse("zhwiki-20161020-pages-meta-current1.xml")
 #   print("Part2...")
 #   parser.parse("zhwiki-20161020-pages-meta-current2.xml")
 #   print("Part3...")
 #   parser.parse("zhwiki-20161020-pages-meta-current3.xml")
 #   print("Part4...")
 #   parser.parse("zhwiki-20161020-pages-meta-current4.xml")
