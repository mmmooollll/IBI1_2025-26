# import necessary l i b r a r i e s 
from matplotlib import cm
import numpy as np 
import matplotlib . pyplot as plt
N = 10000
beta = 0.3
gamma = 0.05
vaccine_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.figure(figsize=(6, 4), dpi=150)
for v in vaccine_rates:
    V = int(N * v)
    S = N - V - 1
    I = 1
    R = 0
    I_hist = [I]
    for t in range(1000):
        if S<=0:
           S = 0
        inf_prob = beta * I / N
        new_inf = np.random.binomial(S, inf_prob)
        new_rec = np.random.binomial(I, gamma)
        
        S -= new_inf
        I += new_inf - new_rec
        R += new_rec
        I_hist.append(I)

    plt.plot(I_hist, label=f'Vaccine {int(v*100)}%')
plt.xlabel('Time')
plt.ylabel('Infected')
plt.title('SIR with Vaccination')
plt.legend()
plt.show()