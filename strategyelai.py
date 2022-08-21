Usage="""
strategyelai.py - version1
Extract elai results like (12      700     700     0.881   0.456   0.453   0.896   0.452) and slide windows sum all
score bigger than 1.5 from all 5 individual.

Usage:
    python strategyelai.py Chr12_3.draw.txt.1 outputfile"""

from sys import argv
import os, math
if len(argv) < 2:
    print (Usage)
else:
    f1 = open(argv[1], 'r')
    f2 = open(argv[2], 'w')
    f2.write("chr\tstart\tend\tsumelai\t>1.5number\n")
    a=f1.read().split('\n')
    b=a[-2].split('\t')[1]
    c=int(int(b)/10000)
    dict={}
    for i in range(1,c+2):
        dict[i]=[]
    for d in a[0:-1]:
        e = d.split('\t')
        f = int(int(e[2])/10000)+1
        if float(e[3]) >= 1.5:
            dict[f].append(e[3])
        if float(e[4]) >= 1.5:
            dict[f].append(e[4])
        if float(e[5]) >= 1.5:
            dict[f].append(e[5])
        if float(e[6]) >= 1.5:
            dict[f].append(e[6])
        if float(e[7]) >= 1.5:
            dict[f].append(e[7])
    for i in range(1,c+2):
        binstart = 1 + (i - 1) * 10000
        binend = i * 10000
        sum=0
        for h in dict[i]:
            sum=sum+float(h)
        f2.write(str(a[0].split('\t')[0])+"\t"+str(binstart)+"\t"+str(binend)+"\t"+str(sum)+"\t"+str(len(dict[i]))+"\n")
    f1.close()
    f2.close()
