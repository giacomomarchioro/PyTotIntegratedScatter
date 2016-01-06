# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:28:22 2016
This is a script to plot the Total Integrated Scatter function.
@author: giacomo
"""

from math import exp, pi,cos #import the exp function note that exp(1)=e, the Euler's Number
import matplotlib.pyplot as plt #import matplotlib for plot the equation
import numpy as np #import numpy for calculating the lambda(lambd)


class TISC:
    """
    This class stores in an instanace all the information to plot the TIS Curve and save the output image.


    Attributes
    ----------
    Rzero: Number
        R0 is the reflectance of the surface. A surface with an higher reflectance has an higher scattering.
    
    wavelenght: Number 
        This is the wavelenght of the radiation used. The plot is in nanometer. 
    
    angle: Number
        Is the angle of incidence of the beam of radiation. If the angle is 0 the beam is perpendicular to the surface.    
    
    lowerlimit: Number
        The lower limit of the plot.
    
    upperlimit: Number
        The higher limit of the plot.
    
    Here an example for a calculation between 0 and 60 nm with an Rzero of 1,wavelenght of 400 nm and angle of incidence 45 degrees.
    
    >>> curve1=TISC(1,400,45,0,60)
    
    
    Methods
    ---------
    
    plot: 
        Use this method to plot the curve.
        
    TIS:
        This is the Total Integrated Scatter formula it is used automatically to plot. 
    
    """
    def __init__(self,Rzero=1,wavelenght=400,angle=45,lowerlimit=0,upperlimit=70,):
        self.Rzero=Rzero        
        self.wavelenght=wavelenght
        self.angle=angle        
        self.lowerlimit=lowerlimit
        self.upperlimit=upperlimit
        if self.angle>90:
            print "--------------------!!WARNING!!------------------------"
            print "----Angle value grater than 90 degrees has been used---"
            print "-------------------------------------------------------"
        self.sigma=np.linspace(self.upperlimit,self.lowerlimit,1000) 
        
    def TIS (self,sigma):
       """
       This is the formula used to calculate the Total Integrated Scatter. 
       """
       return self.Rzero*(1-exp(1)**(-((4*pi*sigma*cos(pi*self.angle/180))/self.wavelenght)**2))*100 
       
    def plot(self):
        """
        This is the plot function that is used to plot the results using Matplotlib. It takes directly all the infomration from the instance of the class.
        
        """
        plt.plot(self.sigma,self.TIS(self.sigma),label=r"$R_{0}=%d$, $\theta=%d\degree$, $\lambda=%s$ nm" %(self.Rzero,self.angle,self.wavelenght)) #plot the function
        plt.legend(loc=2, ncol=1, shadow=True)
        plt.ylabel(r' Total Integrated Scatter (%)')
        plt.xlabel(r'$\sigma (nm)$')
        plt.show() # show the plot

