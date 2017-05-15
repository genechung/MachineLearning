#!/bin/bash
# coding:   utf-8
# Author:   hjy
# Gmail:    haojunyu2012@gmail.com
# Detail:   此脚本用于解决达观培训题一：寻找两个文件中相同的句子


echo "寻找两个文件中相同的句子。。。"
echo "通过hash值切分句子，至于不同的文件中"

rm tmp*
echo "------------------------------------"
time python models/divSortComb_func.py data/f1.dat data/f2.dat 10

echo "------------------------------------"
time python models/divSortComb.py data/f1.dat data/f2.dat 10

echo "------------------------------------"
time python models/sortComb.py data/f1.dat data/f2.dat



