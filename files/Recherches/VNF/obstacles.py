import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt



def larsen(x):
    return np.power(np.cosh(x / 4), -2)


def larsenL(x,L):
    return np.power(np.cosh(x / L), -2)
    
    
def boite(x):
    h = 1
    L = 6
    if x<=0:
        return 0
    elif  0 < x <= L:
        return h
    else :
        return 0


def vancouver(x):
    a = 0.094
    b = 5.94
    c = np.tan(4.5 * np.pi / 180)

    if x < -0.45:
        return 0
    
    elif -0.45<= x < -0.15:
        return (2 * a * (1 - (x + 0.45) - np.exp(-b * (x + 0.45))))
    
    elif -0.15 <= x < 0:
        return (0.1)
    
    elif 0 <= x < 0.34:
        return (2 * a * (1 - (x + 0.3 ) - np.exp(-b * (x + 0.3 ))))
    
    elif x >= 0.34 and x < 1.15:
        return ((2 * a * (1 - (0.34 + 0.3) - np.exp(-b * (0.34 +0.3)))) - (x - 0.34) * c)
    
    else:
        return 0

def acri_2008(x):
    c = np.tan(4.5 * np.pi / 180)
    
    if x < 0:
        return 0
    if 0 <= x < 3.3:
        return  np.tan(18.5 * np.pi / 180) * x

    elif 3.3 <= x < 9.3:
        return  np.tan(18.5 * np.pi / 180) * 3.3

    elif 9.3 <= x < 13.3:
        return  -np.tan(15.5 * np.pi / 180) * x + np.tan(18.5 * np.pi / 180) * 3.3 + np.tan(15.5 * np.pi / 180) * 9.3

    elif  x > 13.3:
        return 0




def acri_2010(x):
    if x <= 0:
        return 0

    elif 0 <= x < 3.288:
        return (np.tan(18.5 * np.pi / 180) * x)

    elif 3.288 <= x < 8.088:
        return (np.tan(18.5 * np.pi / 180) * 3.288)

    elif 8.088 <= x < 16.425:
        return (-np.tan(7.5 * np.pi / 180) * x + np.tan(18.5 * np.pi / 180) * 3.288 + np.tan(7.5 * np.pi / 180) * 8.088)

    elif x > 16.425:
        return 0

    else :
        return 0

    
def Orsay(x):
    h = 0.006569
    if x <= -0.4:
        return 0
    elif -0.4 < x <= -0.25:
        return 0.109035 * np.exp(x * (2.26832 * x + 7.89406)) - h
    elif -0.25 < x <= -0.14:
        return -21002.6 * x**5 - 19498.9 * x**4 - 7188.58 * x**3 - 1320.66 * x**2 - 120.815 * x - 4.30976 - h 
    elif -0.14 < x <= 0.055:
        return 0.08388474 - h
    elif 0.055 < x <= 0.7:
        return 0.0809254 * np.exp(x * (5.44628 * x**2 - 10.59 * x + 1.20697)) + 0.00021074 * x - 0.000012617 - h
    elif 0.7 <x :
        return 0 


if __name__ == "__main__":

    X = np.linspace( 0, 4, 100 )


    bmax = 0.022
    Y = np.array([acri_2010(x, bmax) for x in X])

    print(X)
    print(Y)

    plt.figure()
 
    plt.plot(X, Y, '--')
    plt.xlabel('x')

    plt.show()
