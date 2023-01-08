

import matplotlib.pyplot as plt
import numpy as np


#找出所有可能的点
def triangular_boundary(start,end,n,x_p,y_p):
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

        k=(end[1]-start[1])/(end[0]-start[0])
        x_0=end[0]
        y_0=end[1]
        for i in range(cols):
            if not  possible_point[1,i]<k*(possible_point[0,i]-x_0)+y_0:
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
        d_1=distance_to_segment(point, start, end) 
        
        d_3=np.sqrt(point[0]**2+point[1]**2)-20


        return min(d_1,d_3)




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
      

    return fin_num(n,x_p,y_p)



###############################################################################################################################################
#下面我们来画点
start_1=np.array([20,5.5])
end_1=np.array([44,0])


y=[]
for i in range(11,22):
    y.append(triangular_boundary(start_1,end_1,i,101,101)[1])


x=list(range(11,22))


plt.scatter(x,y)
plt.plot(x,y,label='1')
plt.ylabel('SUM_revison')
plt.xlabel('fin_num')
plt.ylim(0,10)




start_2=np.array([20,5.28])
end_2=np.array([46,0])


y=[]
for i in range(11,22):
    y.append(triangular_boundary(start_2,end_2,i,101,101)[1])


x=list(range(11,22))


plt.scatter(x,y)
plt.plot(x,y,label='2')
plt.ylabel('SUM_revison')
plt.xlabel('fin_num')
plt.ylim(0,10)


start_3=np.array([20,4.91])
end_3=np.array([48,0])
y=[]
for i in range(11,22):
    y.append(triangular_boundary(start_3,end_3,i,101,101)[1])


x=list(range(11,22))


plt.scatter(x,y)
plt.plot(x,y,label='3')
plt.ylabel('SUM_revison')
plt.xlabel('fin_num')
plt.ylim(0,10)





start_4=np.array([20,4.59])
end_4=np.array([50,0])
y=[]
for i in range(11,22):
    y.append(triangular_boundary(start_4,end_4,i,101,101)[1])


x=list(range(11,22))


plt.scatter(x,y)
plt.plot(x,y,label='4')
plt.ylabel('SUM_revison')
plt.xlabel('fin_num')
plt.ylim(0,10)



plt.legend()
plt.show()



























