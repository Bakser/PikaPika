import jieba
import jieba.posseg
import jieba.analyse
import re

class Preprocessor:
    def __init__(self,filename):
        fin = open(filename,'r')
        self.text = fin.read()
        fin.close()
    def rebuild(self):
        self.text = re.sub(r' ',r'',self.text)
    def jieba(self):
        #print '#'.join(jieba.cut(self.text))
        self.words = jieba.posseg.cut(self.text)
        for w in words:
            print w.word+'<'+w.flag+'>',
        print "Keywords:";
        keys = jieba.analyse.extract_tags(self.text,3)
        for w in keys:
            print w


if __name__ == '__main__':
    PC = Preprocessor('input.txt')
    PC.rebuild()
    PC.jieba()
