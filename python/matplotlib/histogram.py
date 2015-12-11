# coding=utf-8
#!/usr/bin/python

# 导入所用模块 -- sys 是常用的模块 
import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


# 代码写在main()里面
def main():
    # 构造数据
    mu = 100
    sigma = 15
    x = mu + sigma * np.random.randn(10000)

    num_bins = 5
    # histogram
    n, bins,patches = plt.hist(x, num_bins, normed=True, facecolor='green',alpha=0.5,label='histogram')
    # 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--',label='poly')
    ## 设置坐标轴
    ## X/Y轴的极限
    xdelt=x.max()-x.min()
    plt.xlim(x.min()-0.1*xdelt,x.max()+0.1*xdelt)
    ## 横纵坐标说明
    plt.xlabel(u'Smarts',fontsize=16)
    plt.ylabel(u'Probability',fontsize=16)
    ## 添加图例
    plt.legend(loc='upper left',frameon=True)
    ## 图的标题
    plt.title(u'直方图',fontsize=20)
    ## 保存图片
    plt.savefig('histogram.jpg')
    ## 显示图片
    plt.show()

# 调用main()函数来启动程序的样板
if __name__ == '__main__':
    main()

