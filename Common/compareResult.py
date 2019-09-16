#! /usr/bin/env python
#coding=GB18030
import sys


reload(sys)
sys.setdefaultencoding('utf8')
file=r'E:\模拟\ReleaseV1.02_20190315\data\fault.txt'
logPath=r'E:\模拟\ReleaseV1.02_20190315\data\log.txt'
f=open(logPath,"w")
print >>f,u'次数'+"    "+'CardNo'+"    "+'CardChannel'
f.close()

with open(file,'r') as f:
    for line in f.readlines():
        if 'Fault' in line:
#             print line
            f = open(logPath,"a")
            print >> f,"           "+line.split(' ')[0]+"        "+line.split(' ')[1]
