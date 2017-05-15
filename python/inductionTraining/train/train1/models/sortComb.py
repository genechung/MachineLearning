#!/usr/bin/python
# coding=utf-8

import sys
import os
from time import time

delimiter = '|@$&|'
def findSame(inFName1, inFName2, outFName):
  start = time()
  # 比较两个文件行数，将行数小的读入内存中
  inFile1 = open(inFName1,'r')
  inFile2 = open(inFName2,'r')
  outFile = open(outFName,'w')
  dict = {}
  counts = 0
  for line in inFile1:
    key = hash(line)
    value = line
    if dict.has_key(key):
      dict[key] = dict[key] + value + delimiter
    else:
      dict[key] = delimiter + value + delimiter

  for line in inFile2:
    key = hash(line)
    value = line
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

  sameSum = findSame(inFName1, inFName2, 'common_sortComb.dat')

  return sameSum

# 调用main()函数来启动程序的样板
if __name__ == '__main__':
  start = time()
  res = main()
  end = time()
  print "sortComb.py执行%s秒，找到相同的句子%d条。" %  ( str(end-start), res )

