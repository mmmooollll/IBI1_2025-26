# import necessary l i b r a r i e s 
import numpy as np 
import matplotlib . pyplot as plt
# make array of all susceptible population
population = np . zeros ( (100 , 100) )
outbreak = np . random . choice (range (100) ,2)
population [ outbreak [ 0 ] , outbreak [ 1 ] ] = 1
plt . figure (figsize=(6 ,4) , dpi =150) 
plt . imshow (population , cmap='viridis' , interpolation='nearest')
size = 100
beta = 0.3
gamma = 0.05
steps = 100
# 0=易感,1=感染,2=康复
pop = np.zeros((size, size))
# 随机初始感染
x, y = np.random.choice(size, 2)
pop[x, y] = 1

# 8邻域偏移
neighbors = [(-1,-1),(-1,0),(-1,1),
             (0,-1),        (0,1),
             (1,-1), (1,0),(1,1)]

for step in range(steps):
    new_pop = pop.copy()
    inf_pos = np.argwhere(pop == 1)
    
    # 感染传播
    for (i,j) in inf_pos:
        for di, dj in neighbors:
            ni = i + di
            nj = j + dj
            if 0<=ni<size and 0<=nj<size:
                if pop[ni, nj] == 0:
                    if np.random.rand() < beta:
                        new_pop[ni, nj] = 1
    
    # 康复
    rec_pos = np.argwhere(pop == 1)
    for (i,j) in rec_pos:
        if np.random.rand() < gamma:
            new_pop[i, j] = 2
    
    pop = new_pop
    
    # 每10步画一张图
    if step % 20 == 0:
        plt.imshow(pop, cmap='viridis', vmin=0, vmax=2)
        plt.title(f'Time {step}')
        plt.axis('off')
        plt.show()
