# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 13:59:31 2023

@author: 86137
"""

def main():
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
                           

        #let's plot
        possible_point=np.array([possible_i,possible_j])
        x=np.array([possible_i])
        y=np.array([possible_j])
        plot=plt.scatter(x, y,s=1)

        #asis equal
        plt.gca().set_aspect(1)
        
        
        
        [rows,cols]=possible_point.shape
        point_num=cols

        return plot , possible_point,point_num
    import numpy as np
    print(generate_point_and_plot(x_p=101 ,y_p=101 ,angle=1/6*np.pi))
if __name__=='__main__':
    main()
