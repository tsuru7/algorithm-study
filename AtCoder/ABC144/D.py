from math import *
a, b, x = list(map(int,input().split()))

theta = 0.0
if (x <= 0.5*a*a*b):
    theta = atan(0.5*a*b*b/x)
else:
    theta = atan( 2.0*(b-x/(a*a))/a )
theta = theta * 180 / pi
print('{:.10f}'.format(theta))
