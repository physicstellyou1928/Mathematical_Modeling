

# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 04:30:37 2023

@author: 86137
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:52:27 2023

@author: 86137
"""




##################################################################################################
#找出所有可能的点
import matplotlib.pyplot as plot
import math
import numpy as np
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



#################################################################################################

#计算点的最短的距离


def d_min(point:np.array):
    start_1,end_1=np.array([20,3]),np.array([38,3])
    start_2,end_2=np.array([38,3]),np.array([38,0])
   

    def distance_to_segment(point,start,end):
        import numpy as np
        import math
        def d(vector):
            return np.sqrt(np.dot(vector,vector))

        def distance_to_point(point,start,end):
            return min(d(point-start),d(point-end))
        #计算点到直线端点距离
        def distance_to_line(point,start,end):
            return abs(np.cross((point-start),(start-end)))/np.sqrt(np.dot((start-end),(start-end)))
        #计算点到直线距离
        if np.dot((start-point),(start-end))>=0 and np.dot((end-point),(end-start))>=0:
            return distance_to_line(point, start,end)
        else:
            return distance_to_point(point, start, end)


    ###################################################################################################
    #下面我们把三个距离都定义出来，之后找出其中最小的一个
    d_1=distance_to_segment(point, start_1, end_1) 
    d_2=distance_to_segment(point, start_2, end_2)    
    d_3=np.sqrt(point[0]**2+point[1]**2)-20


    return min(d_1,d_2,d_3)




##########################################################################################################
#最后我们写一个循环计算所有点的距离和，并且计算平均距离, 这个函数已经封装好了，只需要输入x_p,y_p,n  即可



def fin_num(n,x_p,y_p):
    possible_points=generate_point_and_plot(x_p, y_p, (1/n)*np.pi)[1]
    #此处的[1] 很重要不能忽略
    point_num=generate_point_and_plot(x_p, y_p, (1/n)*np.pi)[0]

    #possible_points[:,i] 就是第i个点的坐标


    SUM=0
    for i in range(point_num):
        SUM=SUM+d_min(possible_points[:,i])

    SUM_revison=SUM/point_num
    return SUM, SUM_revison
  



###############################################################################################################
#让我们画图看看变化趋势，这就是最后的圣杯
y=[]
for i in range(4,28):
    y.append(fin_num(i,101,101)[1])


x=list(range(4,28))


plt.scatter(x,y)
plt.plot(x,y,label='1')
plt.ylabel('SUM_revison')
plt.xlabel('fin_num')
plt.ylim(0,25)


#注：此处可以明显看出当叶片的数量在大于20之后，叶片变化就不是很明显了

##############################################################################################################
#下面我们试试添加一个片数影响函数，f(x)=1+0.02*x
y=[]
for i in range(4,28):
    y.append(fin_num(i,101,101)[1]*(1+0.02*i))


x=list(range(4,28))


plt.scatter(x,y)
plt.plot(x,y,label='2')
plt.ylabel('SUM_revison')
plt.xlabel('fin_num')
plt.ylim(0,25)

#注：此处我们看到变化的趋势在n=15左右趋于平缓
#############################################################################################################
#下面我们试着添加一个更合理一点的影响函数，考虑散热片面积占整个环面的比例（正比与片数n），定义损失函数f(x)=1/(1-x)
y=[]
for i in range(4,28):
    y.append(fin_num(i,101,101)[1]*(1/(1-0.02*i)))


x=list(range(4,28))

print(y)
plt.scatter(x,y)
plt.plot(x,y,label='3')
plt.ylabel('SUM_revison')
plt.xlabel('fin_num')
plt.ylim(0,25)
plt.legend()
plt.show()'''

#下面的分析也挺重要的请看下面

'''
##############################################################################################################
#以及三角型边界是个什么情况
#对于三角行边界d_min的形式发生改变，其他没区别，但是我们还得确定还三角形边界的具体参数


def d_min(point:np.array):
    
    #这里怎末改，却决于我们对具体参数的设定，但是只要参数设定好了，没必要担心三角形的边是斜的
    start_1,end_1=np.array([20,3]),np.array([38,3])
    
   

    def distance_to_segment(point,start,end):
        import numpy as np
        import math
        def d(vector):
            return np.sqrt(np.dot(vector,vector))

        def distance_to_point(point,start,end):
            return min(d(point-start),d(point-end))
        #计算点到直线端点距离
        def distance_to_line(point,start,end):
            return abs(np.cross((point-start),(start-end)))/np.sqrt(np.dot((start-end),(start-end)))
        #计算点到直线距离
        if np.dot((start-point),(start-end))>=0 and np.dot((end-point),(end-start))>=0:
            return distance_to_line(point, start,end)
        else:
            return distance_to_point(point, start, end)


    ###################################################################################################
    #下面我们把三个距离都定义出来，之后找出其中最小的一个
    d_1=distance_to_segment(point, start_1, end_1) 
     
    d_3=np.sqrt(point[0]**2+point[1]**2)-20


    return min(d_1,d_3)
########################################################################

          for i in range(cols):
              if not possible_point[0,i]-2*possible_point[1,i]+5>3 :
          # remove the point in if from the x,y of the possible point
                             possible_i.append(possible_point[0,i])
                             possible_j.append(possible_point[1,i])
                             

'''







