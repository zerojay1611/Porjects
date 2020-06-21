from random import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/x
def loss(x):
    tmp = 1 - x

    if tmp < 0:
        tmp = -1 * tmp

    return tmp

count = 50000
x = []
y = []
inside = 0
S = []
Try = range(1,count+1)
one = []
zero = []
L = []

for i in range(count):
    x.append(uniform(1.0, np.e))
    y.append(random())

    if y[i] < f(x[i]):
        inside += 1
    
    tmp = ((np.e-1)*inside) / (i+1)
    S.append(tmp)
    L.append(loss(S[i]))

    zero.append(0)
    one.append(1)
    
plt.plot(Try, S)
plt.plot(Try, one, linestyle = '--')
plt.plot(Try, L)
plt.plot(Try, zero, linestyle='dotted')
plt.show()

