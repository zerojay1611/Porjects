import numpy as np
import matplotlib.pyplot as plt

def get_hrt(age, hrt, per):
    return (220 - age - hrt)*per + hrt
def numerical_differential(f, x1, x2, x3):
    h = 1e-6

    tmp_x1 = (f(x1+h, x2, x3) - f(x1-h, x2, x3)) / (2*h)
    tmp_x2 = (f(x1, x2+h, x3) - f(x1, x2-h, x3)) / (2*h)
    tmp_x3 = (f(x1, x2, x3+h) - f(x1, x2, x3-h)) / (2*h)

    return [tmp_x1, tmp_x2, tmp_x3]

age = 20
hrt = 85    

tmp_age = []
tmp_hrt = []

percent = np.linspace(0,1,100)

for per in percent:
    print('%d%% : %f' %(int(per*100), get_hrt(age, hrt, per)))
    print(numerical_differential(get_hrt, age, hrt, per))

    tmp_age.append(numerical_differential(get_hrt, age, hrt, per)[0])
    tmp_hrt.append(numerical_differential(get_hrt, age, hrt, per)[1])


plt.plot(percent*100, tmp_age)
plt.plot(percent*100, tmp_hrt, linestyle='--')
plt.show()
