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
    x = np.linspace(-2,2,N)
    y1 = x**3
    y2 = np.sin(x)


    plt.plot(x,y1,'b',marker='*',label='$x^3$',linewidth=2)
    plt.plot(x,y2,'r',marker='+',label='$sin(x)$',linewidth=2)
    ## 设置坐标轴
    ax = plt.gca()  # 获取当前坐标系实例
    # 轴线/标尺设置
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')   # X轴标尺在轴线下面
    ax.spines['bottom'].set_position(('data',0)) # 底部轴线在数据区0的位置
    ax.yaxis.set_ticks_position('left') # Y轴标尺在轴线左边
    ax.spines['left'].set_position(('data',0))  # 左边轴线在数据区0的位置
    ## X/Y轴的极限
    xdelt=x.max()-x.min()
    plt.xlim(x.min()-0.1*xdelt,x.max()+0.1*xdelt)
    ## 横纵坐标说明
    plt.xlabel(u'X',fontsize=16)
    plt.ylabel(u'Y',fontsize=16,rotation='horizontal')
    ## 添加图例
    plt.legend(loc='upper left',frameon=True)
    ## 图的标题
    plt.title(u'折线图',fontsize=20)
    ## 保存图片
    plt.savefig('ploygonal.jpg')
    ## 显示图片
    plt.show()

# 调用main()函数来启动程序的样板
if __name__ == '__main__':
    main()

