# import necessary libraries 
from matplotlib import cm
import numpy as np 
import matplotlib . pyplot as plt
N = 10000 # 总人口数
beta = 0.3 # 感染率
gamma = 0.05 # 康复率
vaccine_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] # 不同疫苗接种率
plt.figure(figsize=(6, 4), dpi=150)# 设置图像大小和分辨率
for v in vaccine_rates:# 模拟不同疫苗接种率下的感染曲线
    V = int(N * v)# 接种疫苗的人数
    S = N - V - 1# 易感人口数
    I = 1# 初始感染人口数
    R = 0 # 初始康复人口数
    I_hist = [I] # 记录每天感染人数
    for t in range(1000): # 模拟1000天
        if S<=0: # 如果没有易感人口了，停止模拟
           S = 0 # 确保S不为负数
        inf_prob = beta * I / N # 计算感染概率
        new_inf = np.random.binomial(S, inf_prob) # 新感染人数
        new_rec = np.random.binomial(I, gamma) # 新康复人数
        S -= new_inf # 更新易感人口数
        I += new_inf - new_rec # 更新感染人口数
        R += new_rec # 更新康复人口数
        I_hist.append(I) # 记录每天感染人数

    plt.plot(I_hist, label=f'Vaccine {int(v*100)}%') # 绘制感染曲线并添加标签
plt.xlabel('Time') 
plt.ylabel('Infected')
plt.title('SIR with Vaccination')
plt.legend()
plt.show()