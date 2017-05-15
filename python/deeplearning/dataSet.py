#!/usr/bin/python
# coding=utf-8

# 导入所用模块 -- sys 是常用的模块 
import sys
import cPickle, gzip, numpy


# 装载数据集
def load_data():
    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    return train_set, valid_set, test_set


# 代码写在m ain()里面
def main():
    train_set, valid_set, test_set = load_data()
    print train_set

# 调用main()函数来启动程序的样板
if __name__ == '__main__':
    main()

