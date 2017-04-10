import json
fin = open('miserables2.json','r')
t = eval(fin.read())
for i in range(0,len(t['nodes'])):
    t['nodes'][i]['id'] = t['nodes'][i]['id'].decode('utf-8')
for i in range(0,len(t['links'])):
    t['links'][i]['source'] = t['links'][i]['source'].decode('utf-8')
#fout.write(t)
#fout.close()
print json.dumps(t,ensure_ascii=False)
#fout = open("miserables2.json",'w')
#fout.write(json.dumps(t,ensure_ascii=False))
#fout.close()
