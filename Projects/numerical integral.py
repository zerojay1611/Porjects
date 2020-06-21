import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(x)
def abs(x):
    if x < 0:
        x *= -1
    return x

count = 1000
start = 0
end = np.log(11)
s = []
dot_g = []

for i in range(count):
    n = abs(end - start) / (i+1)
    s.append(0)
    tmp = start
    dot_g.append(10)

    for j in range(i):
        tmp += n
        s[i] += abs(n * f(tmp))


plt.plot(list(range(count)), s)
plt.plot(list(range(count)), dot_g, linestyle='--')
plt.show()
