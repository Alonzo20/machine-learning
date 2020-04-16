# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager
import matplotlib

font = {'family' : 'MicroSoft YaHei','weight': 'bold','size': 'larger'}
matplotlib.rc("font",family='MicroSoft YaHei',weight="bold")

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(11,31)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels)
plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=0.1)

#展示
plt.show()
