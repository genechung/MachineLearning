#!/usr/bin/python
# coding=utf-8

# 导入所用模块 -- sys 是常用的模块
import sys
from numpy import *

def loadDateSet(fileName):
    '''装载数据

    从文件中获取数据集和标签，文件内容的巴科斯范式（BNF）如下：
    《文件》=《样本数据》《文件》
    《样本数据》= 《特征集》《标签》\n
    《特征集》=《特征》\t《特征集》

    参数：
        filename：  文件名

    返回值：
        xArr：  数据集，(d+1)*n
        yArr:   标签集，1*n

    异常：
        无
    '''

    numFeat = len(open(fileName).readline().split('\t')) - 1
    xArr =[];
    yArr = [];

    fr = open(fileName)
    for line in fr.readlines():
        feaArr = []
        feats = line.strip().split('\t')
        for i in range(numFeat):
            feaArr.append(float(feats[i]))
        xArr.append(feaArr)
        yArr.append(float(feats[-1]))
    return xArr,yArr

# 标准线性回归
def standReg(xArr, yArr):
    '''标准线性回归

    通过矩阵运算直接求解权重，唯一的要求是X^T*X可逆。

    参数：
        xArr：  数据集，(d+1)*n
        yArr:   标签集，1*n

    返回值：
        ws：    权值，(d+1)*1

    异常：
        当X^T*X不可逆/是奇异矩阵，将无法使用矩阵求解
    '''

    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, can't do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws





# 代码写在main()里面
def main():
    # 装载数据集
    X,Y = loadDateSet('ex0.txt')
    ws = standReg(X,Y)
    print ws



# 调用main()函数来启动程序的样板
if __name__ == '__main__':
    main()
