a = 5.08  
b = 5.33  
c = 5.55  
d = b - a  
e = c - b  
# 对比d和e的大小，判断增长趋势
if e < d:
    print("population growth decelerating in Scotland")
elif e > d:
    print("population growth accelerating in Scotland")
else:
    print("population growth is not change in Scotland")
# population growth decelerating in Scotland
X = True
Y = False
W = X or Y
print(W)
#w=True
