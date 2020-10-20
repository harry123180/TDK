import numpy as np
import math
theta = 90
left = 1
right = 1 #rps
d = 113
l = 230
vl = math.pi * d*left
vr = math.pi*d*right


a = np.array([[vl],
             [vr]])
b = np.array([[0.5, 0.5],
              [1/l, 1/l]])
c = np.array([[math.cos(math.radians(theta)),0],
              [math.sin(math.radians(theta)),0],
              [               0            ,1]])
d = np.dot(c,np.dot(b,a)).astype(np.int)
print (d)