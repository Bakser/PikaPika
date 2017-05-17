import re
import sys
import codecs
fin = codecs.open(sys.argv[1],'r','utf-8')
fout = codecs.open(sys.argv[2],'w','utf-8')
#print(fin.readline()[:-1])
fout.write(fin.readline()[:-1]+"\n")
ccnt = 0
for w in fin.readlines():
    res = re.findall(r'^(\d*),(\d*),([^,]*),(\d*)',w)[0]
    lst = res[2].split('/')
    if (len(lst)==1):
        #print(",".join([res[0],res[1],res[2],res[3]]))
        fout.write(",".join([res[0],res[1],res[2],res[3]])+"\n")
    else:
        ccnt += 1
        cnt = 0
        fout.write(",".join(["c"+str(ccnt),res[1],"",res[3]])+"\n")
        for ww in lst:
            cnt += 1
            fout.write(",".join(["c"+str(ccnt)+"-"+str(cnt),"c"+str(ccnt),ww,res[3]])+"\n");

