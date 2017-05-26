import re
import json
import sys

def word_to_path(word):
    lower = word.lower()
    path = "../WikiData/articles/"+lower[0]+"/"
    if (len(word)>1):
        path+=lower[1]+"/"
    else:
        path+="_"+"/"
    if (len(word)>2):
        path+=lower[2]+"/"
    else:
        path+="_"+"/"
    path+=word+".html"
    return path

def search_word(word):
    path = word_to_path(word)
    try:
        with open(path,'r',encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print("Didn't find word "+word)
        return None

class Dealer:
    def __init__(self):
        self.lst = json.load(open('input.json','r',encoding='utf-8'))

    def calculate(self):
        self.text = []
        for i in self.lst:
            self.text.append(search_word(i))
        for i in range(0,len(self.lst)):
            for j in range(0,len(self.text)):
                if (self.text[j] == None):
                    print("-1",end="\t")
                    continue
                else:
                    print(self.text[j].find(self.lst[i]),end="\t")
            print ()

if __name__ == '__main__':
    D = Dealer()
    D.calculate()
