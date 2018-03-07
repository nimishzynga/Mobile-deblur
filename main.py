import numpy as np
import math
# std dev along x axis
sigmaX = 0
# std dev along y axis
sigmaY = 0
t = 0
v = 3
f = 0
x = 0
y = 0

class Deblur:
    def find_equilibrium_factor(self):
        factor1 = v*f*t*math.pi*sigmaX*sigmaY
        val = 2*math.cos(factor1)/v
        self.c = math.log(val)* np.power(x**2+y**2, -6./7)
        return self.c

    def non_linear_deblur(self):






