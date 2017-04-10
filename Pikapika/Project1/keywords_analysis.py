#coding:utf-8
import re
import wikipedia
import langconv
import json

class KeywordsAnalysor:
    def __init__(self):
        wikipedia.set_lang('zh')

    def read_keywords(self,filename = 'keywords_output.txt'):
        fin = open(filename,'r')
        self.wlist = fin.read().decode('utf-8').split('\n')[0:-2]
        fin.close()


    def read_json(self,filename = 'keywords_details.json'):
        fin = open(filename,'r')
        data = json.loads(fin.read())
        self.nodes = data['nodes']
        self.links = data['links']

    def wiki_analysis(self):
        self.nodes = []
        self.links = []
        for w in self.wlist:
            print w
            try:
                text = wikipedia.page(w).content
                text = langconv.Converter('zh-hans').convert(text)
            except wikipedia.exceptions.PageError,e:
                self.nodes.append({'id':'w','wiki':None})
                continue
            except wikipedia.exceptions.DisambiguationError:
                self.nodes.append({'id':'w','wiki':'Too many meaning'})
                continue
            self.nodes.append({"id":w,"group":1,"wiki":text})
    def analyse_words(self):
        for w in self.nodes:
            print w['id']
            if (w['wiki']==None):
                w['type'] == 'Not a keyword'
            if (w['wiki']!=None and len(w['wiki'])<3000):
                w['type'] == 'Not a keyword'

    def build_links(self):
        for w in self.nodes:
            for ww in self.nodes:
                cnt = len(re.findall(ww['id'],w['wiki']))
                if (cnt):
                    self.links.append({"source":w['id'],"target":ww['id'],"value":cnt})

    def export_json(self,filename='keywords_details.json'):
        data = {'nodes':self.nodes,'links':self.links}
        fout = open(filename,'w')
        fout.write(json.dumps(data))
        fout.close()

if __name__ == '__main__':
    KA = KeywordsAnalysor()
    KA.read_keywords()
    #KA.read_json()
    #KA.analyse_words()
    #KA.wiki_analysis()
    #KA.export_json()

