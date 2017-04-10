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
        self.accept = ['title','text']
        self.title_flag = False
        self.pattern = re.compile(':')
        #self.connection= pymysql.connect(host='localhost',user='root',db='wikidb',charset='utf8')
        #self.cursor = self.connection.cursor()
        self.count = 0
        self.fout = open('result.xml','w')
        self.fout.write('<wiki>\n')

    def __del__(self):
        self.fout.write('<wiki>')
        self.fout.close()
        self.cursor.close()
        #self.connection.commit()
        #self.connection.close()

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
            self.title = self.content
        if (self.tag == 'text'):
            self.title_flag = False
            self.text = self.content
            print(self.title,len(self.text))
            lst = re.findall(r'\[\[(\S{1,10}?)\]\]',self.text)
            lst2 = set()
            for w in lst:
                for ww in w.split('|'):
                    lst2.add(ww.lstrip().rstrip())
            self.count += 1
            self.fout.write('<page><title>%s</title><outlinks>%s</outlinks></page>\n'\
                    %(self.title,'|'.join(lst2)))
            '''
            try:
                self.cursor.execute("INSERT INTO keywords(id,word,outlinks) VALUES (%s,%s,%s)", \
                        (self.count,self.title,"|".join(lst2)))
            except pymysql.err.InternalError as e:
                print(e)
            except pymysql.err.IntegrityError as e:
                print(e)
            except pymysql.err.Error as e:
                print(e)
            '''
        #print self.content
        self.content = ''
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
    parser.parse("zhwiki-20161020-pages-meta-current1.xml")
 #   print("Part2...")
 #   parser.parse("zhwiki-20161020-pages-meta-current2.xml")
 #   print("Part3...")
 #   parser.parse("zhwiki-20161020-pages-meta-current3.xml")
 #   print("Part4...")
 #   parser.parse("zhwiki-20161020-pages-meta-current4.xml")
