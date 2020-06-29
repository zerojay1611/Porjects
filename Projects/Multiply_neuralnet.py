import numpy as np

 
#데이터 생성
length_ = 101
a = np.arange(0, 101, 1, np.int)
x_data = np.empty((0, 2), dtype=int)
y_data = np.array([])

for i in range(length_):
    for j in range(length_):
        x_data = np.append(x_data, np.array([[i, j]]), axis=0)
        y_data = np.append(y_data, i*j)


#초기화


