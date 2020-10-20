import math
import numpy as np
theda1 = 60
deg = [ 0,90,0,0,0,0]
base = np.array([[0],
             [0],
             [0],
              [1]])


def transformation_matrix(alpha,a,d,zheta):
    dt = np.dtype(np.float32)
    alpha = math.radians(alpha)
    zheta = math.radians(zheta)
    matrix = np.array([[math.cos(zheta)                , -1*math.sin(zheta)            ,   0              ,           a        ],
                       [math.sin(zheta)*math.cos(alpha),math.cos(zheta)*math.cos(alpha),-1*math.sin(alpha),-1*math.sin(alpha)*d],
                       [math.sin(zheta)*math.sin(alpha),math.cos(zheta)*math.sin(alpha),math.cos(alpha)   , math.cos(alpha)*d  ],
                       [              0                ,              0                ,          0        ,           1        ]],dtype = dt)
    return matrix

T01 = transformation_matrix(0,0,125,deg[0])
T12 = transformation_matrix(90,0,57,deg[1])
T23 = transformation_matrix(0,135,0,deg[2])
T34 = transformation_matrix(90,0,0,deg[3])
T45 = transformation_matrix(-90,0,121,deg[4])
T56 = transformation_matrix(-90,0,20,deg[5])
T22 = T01.dot(T12)
T33 = T22.dot(T23)
T44 = T33.dot(T34)
T55 = T44.dot(T45)
T66 = T55.dot(T56)
print(T66.dot(base))
#print(T12)