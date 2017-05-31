import re
import json
import sys

def word_to_path(word):
    word = word.capitalize()
    lower = word.lower()
    path = "./articles/"+lower[0]+"/"
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

    def __init__(self,lst):
        if type(lst) == list:
            self.lst = lst
        else:
            print(type(lst))

    def calculate(self):
        self.text = []
        res = []
        for i in self.lst:
            self.text.append(search_word(i))
        for i in range(0,len(self.lst)):
            rres = []
            for j in range(0,len(self.text)):
                if (self.text[j] == None):
                    print("-1",end="\t")
                    rres.append(-1)
                    continue
                else:
                    cnt = self.text[j].count(self.lst[i])
                    print(cnt,end="\t")
                    rres.append(cnt)
            print ()
            res.append(rres)
        return res

if __name__ == '__main__':
    D = Dealer(['ubuntu','apple','Linux'])
    D.calculate()
