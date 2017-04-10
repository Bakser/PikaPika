fin = open("dict.txt")
while True:
    line = fin.readline().split(' ')
    if (len(line)!=3):
        break;
    if (int(line[1])>10000):
        print line[0]
