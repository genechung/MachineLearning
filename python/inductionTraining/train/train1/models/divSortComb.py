#!/usr/bin/python
# coding=utf-8

import sys
import os
from time import time

delimiter = '|@$&|'
outFile1 = []
outFile2 = []


# 代码写在main()里面
def main():
  inFName1 = sys.argv[1]
  inFName2 = sys.argv[2]
  outFNums = int(sys.argv[3])
  outFName = 'common_divSortComb.dat'
  print '将文件%s和%s各自切成%d份小文件', (sys.argv[0], sys.argv[1], sys.argv[2])
  divStart = time()
  # 创建输出文件
  for index in range(outFNums):
    outFName1 = "tmp%02d_%s" % (index, os.path.basename(inFName1))
    outFile1.append(open(os.path.join(os.getcwd(),outFName1),'w+'))
    outFName2 = "tmp%02d_%s" % (index, os.path.basename(inFName2))
    outFile2.append(open(os.path.join(os.getcwd(),outFName2),'w+'))

  # 根据每行的hash值分文件
  with open(inFName1,'r') as inFile1:
    for line in inFile1:
      hLine = hash(line)
      # print "hash(%s):%ld" % (line, hLine)
      ind = hLine % outFNums
      outFile1[ind].write("%d\t%s" % (hLine,line))

  with open(inFName2,'r') as inFile2:
    for line in inFile2:
      hLine = hash(line)
      # print "hash(%s):%ld" % (line, hLine)
      ind = hLine % outFNums
      outFile2[ind].write("%d\t%s" % (hLine,line))

  divEnd = time()
  print "[%s]\tDivide File(%s,%s) into %s files" % (str(divEnd-divStart), inFName1, inFName2,  outFNums)
  
  sameSum = 0
  combStart = time()
  # 比较两个文件行数，将行数小的读入内存中
  outFile = open(outFName,'w')
  
  for ind in range(outFNums):
    dict = {}
    outFile1[ind].seek(0)
    outFile2[ind].seek(0)
    for line in outFile1[ind]:
      words = line.split('\t', 1)
      key = words[0]
      value = words[1]
      if dict.has_key(key):
        dict[key] = dict[key] + value + delimiter
      else:
        dict[key] = delimiter + value + delimiter

    for line in outFile2[ind]:
      words = line.split('\t', 1)
      key = words[0]
      value = words[1]
      if dict.has_key(key):
        newValue = delimiter + value + delimiter
        if newValue in dict[key]:
          outFile.write(value)
          sameSum = sameSum + 1
    outFile1[ind].close()
    outFile2[ind].close()
  combEnd = time()
  print "[%s]\tFind [%d] same in files(%s,%s) and write into file(%s)" % (str(combEnd-combStart), sameSum, inFName1, inFName2, outFName)
  outFile.close()
  return sameSum


# 调用main()函数来启动程序的样板
if __name__ == '__main__':
  start = time()
  res = main()
  end = time()
  print "divCombin.py执行%s秒，找到相同的句子%d条。" %  ( str(end-start), res )

