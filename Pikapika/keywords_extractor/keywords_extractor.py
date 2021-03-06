#coding:utf-8
import re
import thulac
from wiki_analyzer.wiki_searcher import WikiSearcher,WikiSearcher_online

'''
基于词性以及开源分词系统，实现名词性短语提取
然后查询离线wiki数据库，判断是否为专业词汇
'''

class KeywordsMiner:
    def __init__(self,filename):
        fin = open(filename,'r')
        self.text = fin.read()
        mthulac = thulac.thulac(user_dict=None, model_path=None, T2S=False, seg_only=False, filt=False)  #默认模式
        lst = mthulac.cut(self.text)
        self.words = []
        for w in lst:
            self.words.append((w[0],w[1]))
        fin.close()

    def get_keywords(self):
        self.keywords = []
        good = ['n','np','ns','ni','nz']
        goodmid = ['s','u','f','n','np','ns','ni','nz','a']
        goodpre = ['s','f','n','np','ns','ni','nz','a']
        l = len(self.words)
        for i in range(0,len(self.words)):
            if (self.words[i][1] in good):
                j = i
                s = ""
                while (j>=0):
                    if (not self.words[j][1] in goodmid):
                        break
                    s = self.words[j][0] + s
                    j = j-1
                    if (len(s)==1):
                        continue
                    if (not self.words[j+1][1] in goodpre):
                        continue
                    self.keywords.append(s)
        self.keywords = list(set(self.keywords))

    def export_keywords(self,filename):
        fout = open(filename,'w')
        for w in self.keywords:
            fout.write(w+'\n')

    def get_TF(self):
        for w in self.keywords:
            cnt = len(re.findall(w,self.text))
            print(cnt)

    def wiki_check(self):
        WS = WikiSearcher()
        update = []
        for w in self.keywords:
            if (WS.exist(w)):
                print(w,"Good!")
                update.append(w)
            else:
                print(w,"Bad!")
                continue
            tt = WikiSearcher_online().get_links(w)
            for w2 in self.keywords:
                if (w2 in tt):
                    print(w,w2)
        self.keywords = update

    def print_keywords(self):
        for w in self.keywords:
            print(w,end='\n')
        print()

if __name__ == '__main__':
    AM = KeywordsMiner('input.txt')
    AM.get_keywords()
    AM.print_keywords()
    AM.wiki_check()
    AM.print_keywords()
    AM.link_check()
    #AM.export_keywords('keywords_output.txt')
