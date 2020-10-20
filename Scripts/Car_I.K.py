import math
speed_of_y = [0,1000,-1000,-1000]

speed_of_x = [0,-1000,-1000,1000]

speed_of_omega  = 10

a = 11.25

b = 5

for i in range(4):
    print(i)
    v1 = speed_of_y[i]-speed_of_x[i]+speed_of_omega*(a+b)
    print('v1=',v1)
    v2 = speed_of_y[i]+speed_of_x[i]-speed_of_omega*(a+b)
    print('v2=',v2)
    v3 = speed_of_y[i]-speed_of_x[i]-speed_of_omega*(a+b)
    print('v3=',v3)
    v4 = speed_of_y[i]+speed_of_x[i]+speed_of_omega*(a+b)
    print('v4=',v4)


    #print(math.atan(speed_of_y/speed_of_x)*180/3.14159)





