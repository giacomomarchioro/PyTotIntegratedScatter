# PyTotIntegratedScatter
These are two simple scripts to plot the total integrated scatter vs. Surface roughness.
There are two main files:

###TISClass.py

The function is inside a class so you have to create an instance and use the method ´plot´ to plot the curve.
Like this:

```python 
 >>> curve1=TISC(1,400,45,0,60)#passing Rzero, wavelenght, angle, lowerlimit, upperlimit
 >>> curve1.plot()
```


###TIS.py

This is a simple script that you can eventually ran changing the parameters directly on the script.



