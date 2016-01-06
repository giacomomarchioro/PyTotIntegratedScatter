# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:21:05 2016

@author: giacomo
"""

from math import exp, pi,cos
import matplotlib.pyplot as plt #import matplotlib for plot the equation
import numpy as np 

upperlimit=0 #upper limit, the shortest wavelenght, in nm 
lowerlimit=60 #lower limit, the longhest waveleght, in nm
Rq=np.linspace(upperlimit,lowerlimit,1000) #
Rzero=1
wavelenght=4000#nm
angle=10

       
def TIS(Rq):
             return Rzero*(1-exp(1)**(-((4*pi*Rq*cos(pi*angle/180))/wavelenght)**2))*100 #Planck's law for wavelenght note that wavelenght is in meters


plt.plot(Rq,TIS(Rq),label=r"$R_{0}=%d$, $\theta=%d\degree$, $\lambda=%s$ nm" %(Rzero,angle,wavelenght)) #plot the function
plt.legend(loc=0, ncol=1, shadow=True)
       

plt.ylabel(r' Total Integrated Scatter (%)')
plt.xlabel(r'$R_{q}(nm)$')
plt.show() # show the plot
savefig("corponero150dpi.png",dpi=150)