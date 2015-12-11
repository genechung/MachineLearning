# coding=utf-8
#!/usr/bin/python

# 导入所用模块 -- sys 是常用的模块 
import sys
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


# 代码写在main()里面
def main():
    # 构造数据
    N = 50
    x = np.arange(N)
    y1 = np.random.rand(N)*25
    y2 = np.random.rand(N)*25+25


    plt.scatter(x,y1,s=50,c='b',marker='+',alpha=0.5,label='ClassA')
    plt.scatter(x,y2,s=100,c='r',marker='.',alpha=0.5,label='ClassB')
    
    ## X/Y轴的极限
    xdelt=x.max()-x.min()
    plt.xlim(x.min()-0.1*xdelt,x.max()+0.1*xdelt)
    plt.ylim(0,50)
    ## 横纵坐标说明
    plt.xlabel(u'x值说明',fontsize=16)
    plt.ylabel(u'y值说明',fontsize=16,rotation='horizontal')
    ## 添加图例
    plt.legend(loc='upper left',frameon=True)
    ## 图的标题
    plt.title(u'scatter图',fontsize=20)
    ## 保存图片
    plt.savefig('scatter.jpg')
    ## 显示图片
    plt.show()

# 调用main()函数来启动程序的样板
if __name__ == '__main__':
    main()

