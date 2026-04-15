# import necessary l i b r a r i e s 
import numpy as np 
import matplotlib . pyplot as plt
N = 10000
beta = 0.3
gamma = 0.05
S = N - 1
I = 1
R = 0
S_list = [S]
I_list = [I]
R_list = [R]
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