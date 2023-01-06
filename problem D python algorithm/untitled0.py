# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:35:44 2023

@author: 86137
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,50,51)
y=np.linspace(0, 50,51)
Y,X=np.meshgrid(x,y)

a=X**2+Y**2

# print('this line is a')  /  print(a)





'''
print(a[1,2])
print(bool(a[1,2]<2500))
print(int(a[1,9]))

print(type(a))
t=a[10]
print(t)
'''


'''
this is the first part
'''

#very important
[rows,cols]=a.shape
# print(rows,cols)

possible_i=[]
possible_j=[]


#loop
for i in range(rows):
    for j in range(cols):
#logical althoroty
        if 400<a[i,j]<2500:
            #print(i,j)
            possible_i.append(i)
            possible_j.append(j)
#print(possible_i)
#print(possible_j)
possible_point=np.array([possible_i,possible_j])
#  print(possible_point)



'''
this is the second part
'''



[rows,cols]=possible_point.shape
# print(rows,cols)

possible_i=[]
possible_j=[]

for i in range(cols):
    if possible_point[1,i]<0.5*possible_point[0,i]:
        possible_i.append(possible_point[0,i])
        possible_j.append(possible_point[1,i])
        
print('\t this the second part parameter')        
print(possible_i) 
print(possible_j)
        
'''
for possilbe_point
the element in the first row (row no.0) is the x-coordinate of the point
the element in the second row (row no.1) is the y-coordinate of the point
'''
possible_point=np.array([possible_i,possible_j])
print('\t this is the second part possible_point ')
print(possible_point)
print('\t the second part possible_point is over')


'''
this is the third part
'''


[rows,cols]=possible_point.shape
print(rows,cols)



for i in range(cols):
    if possible_point[0,i]<=38 and possible_point[1,i]<3 :
# remove the point in if from the x,y of the possible point
                    possible_i.pop(possible_point[0,i])
                    possible_j.pop(possible_point[1,i])

possible_point=np.array([possible_i,possible_j])
print('\t this is the second part possible_point ')
print(possible_point)
print('\t the third (maybe final) part possible_point is over')

[rows,cols]=possible_point.shape
print(rows,cols)







#let's plot

x=np.array([possible_i])
y=np.array([possible_j])
plt.scatter(x, y,s=1)

#asis equal

plt.gca().set_aspect(1)

plt.show()
       







