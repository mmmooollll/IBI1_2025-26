# import necessary libraries 
import numpy as np # 随机数
import matplotlib . pyplot as plt # 绘图工具
N = 10000 # 总人口数
beta = 0.3 # 感染率
gamma = 0.05 # 康复率
S = N - 1 # 易感人口数
I = 1 # 感染人口数
R = 0 # 康复人口数
S_list = [S]
I_list = [I]
R_list = [R]# 记录每天各类人口数
for _ in range(100):
    new_infections = np.random.binomial(S, beta * I / N) # 新感染人数
    new_recoveries = np.random.binomial(I, gamma) # 新康复人数
    S -= new_infections # 更新易感人口数
    I += new_infections - new_recoveries # 更新感染人口数
    R += new_recoveries # 更新康复人口数
    S_list.append(S) # 记录易感人口数
    I_list.append(I) # 记录感染人口数
    R_list.append(R) # 记录康复人口数
plt.figure(figsize=(6, 4), dpi=150 )
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('SIR Model Simulation')
plt.legend()
plt.show()