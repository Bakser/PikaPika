#encoding=utf-8
import sys
import re
import thulac
import json
import codecs
from Searcher.searcher import *
class pika:
    types={'n','np','ns','ni','nz','j'}#'a'
    thu_cut=thulac.thulac()
    def __init__(self,_text):
        #fin=open(nm,'r')
        self.text=_text
        #fin.close()
    def cut_words(self):
        wordslistpre=self.thu_cut.cut(self.text)
        self.wordslist=[x[0] for x in wordslistpre if x[1] in self.types]
    def cut_sectences(self):
        last=0
        cnt=0
        self.sectences=[]
        for i in range(0,len(self.text)):
            if self.text[i] in {'(','（'}:
                cnt+=1
            elif self.text[i] in {')','）'} and cnt>0:
                cnt-=1
            if cnt==0 and self.text[i] in {'.','?','!','。','？','…'}:
                if i-last>1:
                    self.sectences.append(self.text[last:i])
                last=i+1
        self.cut_s=[]
        for i in self.sectences:
            self.cut_s.append([x[0] for x in self.thu_cut.cut(i) if x[1] in
                               self.types])
    def prt(self):
        fout=codecs.open('tst','w',"utf-8")
        for i in self.sectences:
            fout.write(str([x[0] for x in self.thu_cut.cut(i) if x[1] in
                            self.types]))
        fout.close()
    def __str__(self):
        return str(self.text)
class textrank(pika):
    slides_width=3
    damping=0.85
    iteration_times=300
    result_numbers=10
    wikiFactor=2
    def __init__(self,nm):
        super().__init__(nm)
    def word_cloud(self,filename):
        self.cut_words()
        self.worddict=dict()
        for i in self.wordslist:
            if not i in self.worddict:
                self.worddict[i]=0
            self.worddict[i]+=1
        res=[]
        for i in self.worddict:
            res.append((i,self.worddict[i]))
        fout=codecs.open(filename,"w","utf-8")
        fout.write(json.dumps(res,ensure_ascii=False))
        fout.close()
        return
    def build_graph(self,cutlist):
        K=self.slides_width
        self.G=dict()
        self.wiki=dict()
        for i in cutlist:
            if i.__name__!="str":
                print(i,"utf-8")
        wikiDealer=Dealer(cutlist)
        mat=wikiDealer.calculate()
        for i in range(0,len(cutlist)):
            p=cutlist[i]
            if mat[i][0]==-1:
                self.wiki[p]=1.0
                continue
            if not p in self.G:
                self.G[p]=dict()
            self.wiki[p]=self.wikiFactor
            tsum=0
            for j in mat[i]:
                tsum+=j
            for j in range(0,len(cutlist)):
                if not cutlist[j] in self.G[p]:
                    self.G[p][cutlist[j]]=float(mat[i][j])/float(tsum)*self.wikiFactor
        for s in cutlist:
            for i in range(0,len(s)):
                p=s[i]
                if not p in self.G:
                    self.G[p]=dict()
                for j in range(max(i-K,0),min(i+K,len(s)-1)):
                    if not s[j] in self.G[p]:
                        self.G[p][s[j]]=1.0*self.wiki[s[j]]
                    else:
                        self.G[p][s[j]]+=1.0*self.wiki[s[j]]
       
            
    def print_graph(self):
        for i in self.G:
            print(i,':',self.G[i].items())
    def calc(self,source,dest):
        d=self.damping
        for i in dest:
            dest[i]=1.0-d
        for u in self.G:
            tot=0.0
            for v in self.G[u]:
                tot+=self.G[u][v]
            if tot==0.0:
                continue
            tot=source[u]*d/tot
            for v in self.G[u]:
                dest[v]+=self.G[u][v]*tot
    def evaluate(self,cutlist):
        tot=self.iteration_times
        self.val=[dict(),dict()]
        for i in cutlist:
            for j in i:
                if not j in self.val[0]:
                    self.val[0][j]=1.0
                else:
                    self.val[0][j]+=1.0
        self.val[1]=self.val[0].copy()
        now=0
        for t in range(0,tot):
            self.calc(self.val[now],self.val[now^1])
            now^=1
        self.res=sorted(self.val[now^1].items(),key=lambda x:x[1],reverse=True)
    def init(self,sentences=True):
        if sentences:
            self.cut_sectences()
            self.build_graph(self.cut_s)
            self.evaluate(self.cut_s)
        else:
            self.cut_words()
            self.build_graph(self.wordslist)
            self.evaluate(self.wordslist)
    def query(self):
        nres=[]
        k=self.result_numbers
        for i in range(0,min(k,len(self.res))):
            nres.append(self.res[i][0])
        return nres
class parser:
    pat_list=[re.compile(r"^(([\d一二三四五六七八九十][.:。、．：\s]){1}|摘要|总结|Abstract|abstract|Summary|summary)"),re.compile(r"^[\d一二三四五六七八九十][.:。、．：\s][\d一二三四五六七八九十][.:。、．：\s]*"),re.compile(r"^[\d一二三四五六七八九十][.:。、．：\s][\d一二三四五六七八九十][.:。、．：\s][\d一二三四五六七八九十][.:。、．：\s]*")]
    pat_abstract=re.compile(r"^(摘要|Abstract|abstract)")
    max_line_len=60
    def __init__(self,nm):
        fin=codecs.open(nm,'r',"utf-8")
        self.lines=fin.read().split('\n')
        To_Filter=["\r","\n","\t"]
        for i in To_Filter:
            for s in self.lines:
                s=s.replace(i,"")
        self.lines=[i for i in self.lines if i!=""]
        fin.close()
    def cut_paragraph(self):
        max_len=max([len(i) for i in self.lines])
        print(max_len)
        for i in self.lines:
            print(i)
    def jud_title(self,line):
        for i in range(0,3):
            if self.pat_list[2-i].match(line):
                return 3-i
        return 4
    def cut_titles(self):
        res=[]
        tmp=""
        for i in self.lines:
            if self.pat_abstract.match(i):
                continue
            title_level=self.jud_title(i)
            if title_level!=4:
                if tmp!="":
                    res.append((4,tmp))
                    tmp=""
                res.append((title_level,i))
            elif len(i)>self.max_line_len:
                res.append((4,tmp+i))
                tmp=""
            else:
                tmp+=i
        if tmp!="":
            res.append((4,tmp))
        rres=[]
        for i in res:
            if i[0]==4:
                t=textrank(i[1])
                t.init()
                rres.append((4,t.query()))
            else:
                rres.append((i[0],[i[1]]))
        self.max_list_len=len(rres)
        return rres
    def trans(self,x):
        res=""
        for i in range(0,len(x)):
            res+=x[i]
            if i!=len(x)-1:
                res+='/'
        return res
    def build_tree(self):
        tmp=self.cut_titles()
        last=[[] for i in range(0,5)]
        last[0].append(0)
        for i in range(0,5):
            last[i].append(-1)
        for i in range(0,len(tmp)):
            for j in range(0,5):
                if tmp[i][0]==j:
                    last[j].append(i+1)
                else:
                    last[j].append(last[j][i])
        Res=["0,,"+str(self.lines[0])+",0"]
        #print(''.join([self.lines[0],"0"]))
        #print("0,,"+self.lines[0]+",0")
        for i in range(0,len(tmp)):
            mxval=0
            for j in range(0,tmp[i][0]):
                mxval=max(last[j][i],mxval)
            Res.append(str(i+1)+","+str(mxval)+","+self.trans(tmp[i][1])+","+str(tmp[i][0]))
        return Res
    def output(self,filename):
        Res=self.build_tree()
        fout=codecs.open(filename,"w","utf-8")
        fout.write("id,parentid,text,value\n")
        for i in range(0,len(Res)):
            if i==len(Res)-1:
                fout.write("%s"%Res[i])
            else:
                fout.write("%s\n"%Res[i])
        fout.close()
if __name__=='__main__':
    if len(sys.argv)<2:
        print("Usage main.py text.in cloud.out tree.out")
    #t=textrank(sys.argv[1])
    #t.init()
    #t.query()
    #t=cutter(sys.argv[1])
    print("Begin...");
    inputfilename = sys.argv[1]
    cloud_output = sys.argv[2]
    tree_output = sys.argv[3]
    print("Input file:",inputfilename)
    print("Output file:",cloud_output,tree_output)
    text_fin=codecs.open(inputfilename,"r","utf-8")
    t=textrank(text_fin.read())
    print("Init...");
    t.init()
    t.word_cloud(cloud_output)
    text_fin.close()
    parser(inputfilename).output(tree_output)
    print("Finish...");
    #print(json.dumps(l,ensure_ascii=False))
