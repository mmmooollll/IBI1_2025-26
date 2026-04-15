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
    new_infections = np.random.binomial(S, beta * I / N)
    new_recoveries = np.random.binomial(I, gamma)
    S -= new_infections
    I += new_infections - new_recoveries
    R += new_recoveries
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
plt.figure(figsize=(6, 4), dpi=150 )
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('SIR Model Simulation')
plt.legend()
plt.show()