import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter 


def sigmoid(x):
	return 1/(np.exp(-x)+1)

def tanh(x):
	return 2*sigmoid(2*x)-1



x = np.arange(-10.0, 10.0, 0.1)
y = tanh(x)
# y = np.arctan(x)


xmajorLocator   = MultipleLocator(2) #将x主刻度标签设置为20的倍数  
xmajorFormatter = FormatStrFormatter('%d') #设置x轴标签文本的格式  
xminorLocator   = MultipleLocator(1) #将x轴次刻度标签设置为5的倍数  
  
ymajorLocator   = MultipleLocator(0.5) #将y轴主刻度标签设置为0.5的倍数  
ymajorFormatter = FormatStrFormatter('%1.1f') #设置y轴标签文本的格式  
yminorLocator   = MultipleLocator(0.1) #将此y轴次刻度标签设置为0.1的倍数  

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2)

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.ylim(-1.2, 1.2)

#设置主刻度标签的位置,标签文本的格式  
ax.xaxis.set_major_locator(xmajorLocator)  
ax.xaxis.set_major_formatter(xmajorFormatter)  
  
ax.yaxis.set_major_locator(ymajorLocator)  
ax.yaxis.set_major_formatter(ymajorFormatter)  

#显示次刻度标签的位置,没有标签文本  
ax.xaxis.set_minor_locator(xminorLocator)  
ax.yaxis.set_minor_locator(yminorLocator) 

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none') 
plt.show()