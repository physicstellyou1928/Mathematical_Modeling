# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 05:01:24 2023

@author: 86137
"""

import matplotlib.pyplot as plt
import numpy as np

'''

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]
plt.scatter(x,y)
plt.scatter(x2,y2)



plt.plot(x, y, label='1')
plt.plot(x2, y2, label='Second Line')

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()




'''


def generate_point_and_plot(x_p ,y_p ,angle):

    
    import matplotlib.pyplot as plt
    import numpy as np
    x=np.linspace(0,50,x_p)
    y=np.linspace(0, 50,y_p)
    Y,X=np.meshgrid(x,y)

    a=X**2+Y**2

    #very important
    [rows,cols]=a.shape

    possible_i=[]
    possible_j=[]


    #loop
    for i in range(rows):
        for j in range(cols):
    #logical algorithm
            if 400<a[i,j]<2500:
                #print(i,j)
                possible_i.append((50/(x_p-1))*i)
                possible_j.append((50/(y_p-1))*j)
 
    possible_point=np.array([possible_i,possible_j])



    [rows,cols]=possible_point.shape
    # print(rows,cols)

    possible_i=[]
    possible_j=[]

    for i in range(cols):
        if possible_point[1,i]<np.tan(angle)*possible_point[0,i]:
            possible_i.append(possible_point[0,i])
            possible_j.append(possible_point[1,i])
            
    possible_point=np.array([possible_i,possible_j])
    
    
    
    # the third part
    
    
    [rows,cols]=possible_point.shape
    
    possible_i=[]
    possible_j=[]

    for i in range(cols):
        if not possible_point[0,i]<38 or possible_point[1,i]>3 :
    # remove the point in if from the x,y of the possible point
                       possible_i.append(possible_point[0,i])
                       possible_j.append(possible_point[1,i])
                       
                       
    

    possible_point=np.array([possible_i,possible_j])
     
    [rows,cols]=possible_point.shape
    point_num=cols


    

    return point_num, possible_point, possible_i, possible_j



points_x=generate_point_and_plot(101 ,101 ,1/6*np.pi)[2]
points_y=generate_point_and_plot(101 ,101 ,1/6*np.pi)[3]


plt.scatter(points_x,points_y,s=0.5)
plt.xlim(0,50)
plt.xlim(0,50)
plt.xlabel('x')
plt.ylabel('y')

x_ticks=range(0,50,5)
y_ticks=range(0,50,10)

plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.title('here is the title')

plt.show()

##################################################################################################
#现在我的麻烦是如何画出边界线















































