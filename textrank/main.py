#encoding=utf-8
import sys
import thulac
class pika:
    types={'n','np','ns','ni','nz','j','a'}
    thu_cut=thulac.thulac()
    def __init__(self,nm):
        fin=open(nm,'r')
        self.text=fin.read()
        fin.close()
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
        fout=open('tst','w')
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
    result_numbers=5
    def __init__(self,nm):
        super().__init__(nm)
    def build_graph(self,cutlist):
        K=self.slides_width
        self.G=dict()
        for s in cutlist:
            for i in range(0,len(s)):
                p=s[i]
                if not p in self.G:
                    self.G[p]=dict()
                for j in range(max(i-K,0),min(i+K,len(s)-1)):
                    if not s[j] in self.G[p]:
                        self.G[p][s[j]]=1.0
                    else:
                        self.G[p][s[j]]+=1.0
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
        k=self.result_numbers
        for i in range(0,k):
            print(self.res[i])
if __name__=='__main__':
    t=textrank(sys.argv[1])
    t.init()
    t.query()