#!/usr/bin/python
# coding=utf-8

import sys
import os
from time import time

delimiter = '|@$&|'
def divFile(inFName, outFNums):
  start = time()
  outFile = []
  # 创建输出文件
  for index in range(outFNums):
    outFName = "tmp%02d_%s" % (index, os.path.basename(inFName))
    outFile.append(open(os.path.join(os.getcwd(),outFName),'w'))

  # 根据每行的hash值分文件
  with open(inFName,'r') as inFile:
    for line in inFile:
      hLine = hash(line)
      # print "hash(%s):%ld" % (line, hLine)
      ind = hLine % outFNums
      outFile[ind].write("%d\t%s" % (hLine,line))

  # 关闭输出文件
  for index in range(outFNums):
    outFile[index].close()
  end = time()
  print "[%s]\tDivide File(%s) into %s files" % (str(end-start), inFName, outFNums)


def findSame(inFName1, inFName2, outFName):
  start = time()
  # 比较两个文件行数，将行数小的读入内存中
  inFile1 = open(inFName1,'r')
  inFile2 = open(inFName2,'r')
  outFile = open(outFName,'w')
  dict = {}
  counts = 0
  for line in inFile1:
    words = line.split('\t', 1)
    key = words[0]
    value = words[1]
    if dict.has_key(key):
      dict[key] = dict[key] + value + delimiter
    else:
      dict[key] = delimiter + value + delimiter

  for line in inFile2:
    words = line.split('\t', 1)
    key = words[0]
    value = words[1]
    if dict.has_key(key):
      newValue = delimiter + value + delimiter
      if newValue in dict[key]:
        outFile.write(value)
        counts = counts + 1
  end = time()
  print "[%s]\tFind [%d] same in files(%s,%s) and write into file(%s)" % (str(end-start), counts, inFName1, inFName2, outFName)
  return counts

# 代码写在main()里面
def main():
  inFName1 = sys.argv[1]
  inFName2 = sys.argv[2]
  fileNums = sys.argv[3]

  print '将文件%s和%s各自切成%d份小文件', (sys.argv[0], sys.argv[1], sys.argv[2])
  divFile(inFName1, int(fileNums))
  divFile(inFName2, int(fileNums))
  
  sameSum = 0
  for ind in range(int(fileNums)):
    fName1 = "tmp%02d_%s" % (ind, os.path.basename(inFName1))
    fName2 = "tmp%02d_%s" % (ind, os.path.basename(inFName2))
    sameSum += findSame(fName1, fName2, 'common.dat')
  return sameSum

# 调用main()函数来启动程序的样板
if __name__ == '__main__':
  start = time()
  res = main()
  end = time()
  print "divCombin.py执行%s秒，找到相同的句子%d条。" %  ( str(end-start), res )

