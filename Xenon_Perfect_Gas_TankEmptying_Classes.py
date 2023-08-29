# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:56:38 2023

@author: Philippe.Lott
"""

import matplotlib.pylab as plt
import numpy as np
from tanklib import myTank
from gaslib import myPerfectGas, myVdWGas       

P1 = 10000 # Initial Pressure (Pa)
T1 = 273 # Initial Temperature (K)
n = 1000 # Moles
f = 0.01 # Moles/Step
R = 8.3144598 # Ideal Gas Constant
g = 1.4 # Gamma for Xenon
it = int(n/f -1) # Number of iterations
sc = 1e-3
f_ = [0.001,0.01,0.1,1,10,100]
it00,t00,p00= [],[],[]

VdW = False

for f0 in f_:
    print(f0)
    it = int(n/f0-1)
    if not VdW:
       Xenon2 = myPerfectGas(g, 1, 1)
    else:
       Xenon2 = myVdWGas(g,1,1,4.192*sc,0.0516*sc)
    Tank2 = myTank(Xenon2, P1, T1,n0=n)
    steps = np.zeros(it)+f0
    Tank2.iterate(steps)
    t00.append(np.asarray(Tank2.T_))
    p00.append(np.asarray(Tank2.P_))
    it00.append(np.linspace(0,1,it+1))

plt.figure()

for t0,it0 in zip(t00,it00):
    plt.plot(it0,t0,label="Perfect Gas")
plt.xlabel("No Dim Time")
plt.ylabel("Temperature")
plt.show()

plt.figure()

for t0,it0 in zip(p00,it00):
    plt.plot(it0,t0,label="Perfect Gas")
plt.xlabel("No Dim Time")
plt.ylabel("Pressure")
plt.show()


"""
#Xenon = myPerfectGas(g, 1, 1)
Xenon = myVdWGas(g,1,1,4.192*sc,0.0516*sc)
Tank = myTank(Xenon, P1, T1,n0=n)
steps = np.zeros(it)+f
Tank.iterate(steps)

Xenon2 = myPerfectGas(g, 1, 1)
Tank2 = myTank(Xenon2, P1, T1,n0=n)
steps = np.zeros(it)+f
Tank2.iterate(steps)

s = np.linspace(0,1,it+1)
plt.figure()
plt.plot(s,Tank.T_,label="VdW")
plt.plot(s,Tank2.T_,label="Perfect Gas")
plt.legend(loc="best")
plt.xlabel("No Dim Time")
plt.ylabel("Temperature")
plt.show()

plt.figure()
plt.plot(s,Tank.P_,label="VdW")
plt.plot(s,Tank2.P_,label="Perfect Gas")
plt.legend(loc="best")
plt.xlabel("No Dim Time")
plt.ylabel("Pressure")
plt.show()   
"""   