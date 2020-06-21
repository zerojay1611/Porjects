import numpy as np

def Expect(n, W, L):
    return W**n / (W**n + L**n)
def softmax(W, L):
    n = 1.1
    tmp = max([W, L])
    return n**(W - tmp) / (n**(W - tmp) + n**(L - tmp))

def numerical_differential(f, n, W, L):
    h = 1e-6

    tmp_n = (f(n+h, W, L) - f(n-h, W, L)) / (2*h)
    tmp_W = (f(n, W+h , L) - f(n, W-h, L)) / (2*h)
    tmp_L = (f(n, W, L+h) - f(n, W, L-h)) / (2*h)

    return [tmp_n, tmp_W, tmp_L]
def numerical_differential_(f, W, L):
    h = 1e-6

    tmp_W = (f(W+h, L) - f(W-h, L)) / (2*h)
    tmp_L = (f(W, L+h) - f(W, L-h)) / (2*h)

    return [tmp_W, tmp_L]

n = 9
while True:
    W, L = float(input('W : ')), float(input('L : '))

    print('Expect: %f, softmax: %f' %(Expect(n, W, L), softmax(W, L)))
    print('Expect_d: ' , numerical_differential(Expect, n, W, L))
    print('softmax_d: ', numerical_differential_(softmax, W, L))
