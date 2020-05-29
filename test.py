import numpy as np


b=np.random.rand(1)#0到1的均匀分布
print(b)

if b < 0.7:
    print("yes")
else:
    print("no")