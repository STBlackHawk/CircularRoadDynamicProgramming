#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 01:07:32 2019

@author: blackhawk
"""

#Section2
#This question was ambigous there was not clear whether I have to only 
#not compute one of combinations after T round based on the equal probability 
#of choices or all the combination so I solved both ways I have to 
#compute all possible values.

import numpy as np
import random as rd
import copy
import time
import math


# Since "Expected Value" has been requested I think the right is to 
#calculate average and standard deviation for all possible answers not only
#I wrote the code for the all possible answers in section 1 but also I wrote the code for 
#the simle way which we only calculate the average and standard deviation 
#of the last position on 1 possible answer in section 2


   
#1 In this section because the combination of possible answeres are really 
#big I used divide and conquer technique using recursive function and 
#memoization technique to solve this problem and in each stepI pass average,
#probabilistic standard deviation, probabilistic standard deviation 
#of average and standard and probabilistic deviation of standard deviation
 
def Circular_Road_Car(N, M, T):
    
    #Creating variables and position list 
    position= bool
    
    position = [0] * N
    
    #memoization hashtable using positions and round as key to average, std, ...
    global memoizedpos
    
    memoizedpos = {}
    
    #Creating position 
    for i in range(0, M):
        position[i] = True
        
    answer = Rec_Circular_road_car(N, T, position)
    
    print(answer)




def Rec_Circular_road_car(N, T, p):

    roadLen = N
    rounds = T
    position = p
    positionidx = []
    tposition = tuple(position)
    
    if (tposition,rounds) in memoizedpos:
        return list(memoizedpos[tposition,rounds])

    if rounds == 0: 
          
            for i in range(0, roadLen):
                if position[i] : 
                    positionidx.append(i)
            aver = np.mean(positionidx) 
            sd = np.std(positionidx)
            
            memoizedpos[tposition , rounds] = tuple([aver, sd, 0, 0])
            rlist = [aver, sd, 0, 0]
            return rlist
                
    averlist = []
    stdlist = []
    averstdlist = []
    stdstdlist = []
    funclist = [] 
        
    for j in range (0, roadLen):
            next = (j + 1) % roadLen
            
            if (position[j] and not position[next]): 
                pos = copy.deepcopy(position)
                pos[j]= False
                pos[next] = True
                r = rounds - 1
                funclist = []
                funclist = Rec_Circular_road_car(roadLen, r, pos)
              
                if funclist[0]: averlist.append(funclist[0])
                if funclist[1]: stdlist.append(funclist[1])
                if funclist[2]: averstdlist.append(funclist[2])
                if funclist[3]: stdstdlist.append(funclist[3])
      
    aver = np.mean(averlist)
        
    sd = math.sqrt(sum(k*k for k in stdlist))/len(stdlist)
        
        #If it is the one round before last function from round T will return 0 for 
        #the standard devation of the average so if they return zero we need to
        #buid the first standard deviation of means on the rounf T-1
    if all([ v == 0 for v in averstdlist ]): averstd = np.std(averlist)
    else:  averstd = math.sqrt(sum(m*m for m in averstdlist))/len(averstdlist)
        
        
    if all([ n == 0 for n in stdstdlist ]): stdstd = np.std(stdlist)
    else:  stdstd = math.sqrt(sum(q*q for q in stdstdlist))/len(stdstdlist) 

    memoizedpos[tposition , rounds]= tuple([aver, sd, averstd, stdstd])
    return [aver, sd, averstd, stdstd]
    
    
    
    
    Circular_Road_Car(10, 5,20)
    
    
    
#2

def Simple_Circular_Road_Car(N, M, T)
    cars = M
    roadLen = N
    rounds = T
    CircularRoud = bool
    CircularRoud =[0] * roadLen
    position = int
    position = [0]* cars
    #Avl = np.zeros((1,5), dtype = bool)
    PossibleCars = []
    average = []
    Std = []
    
    
    
    QueueCar = M
    

    for i in range (0,rounds): 
       if QueueCar > 0 : CircularRoud[0] = True
       for j in range(0,roadLen): 
            if CircularRoud[j]:
                if j == CircularRoud[roadLen-1]: 
                    if not CircularRoud[0]: 
                        PossibleCars.append(position.index(j))
                
                    else: 
                        if not CircularRoud[j+1]:
                            PossibleCars.append(position.index(j))
                
        
     
        
        
                k = rd.choice(PossibleCars)
      
                if (position[k] == 0 and QueueCar > 0): QueueCar -=1
               
                CircularRoud[position[k]] = False
                
                if  position[k] == roadLen-1 :
                    CircularRoud[0] = True
                    position[k] = 0
                else :    
                    CircularRoud[position[k]+1] = True
                    position[k] +=1
                
                average.append(np.mean(position))
                Std.append(np.std(position))
                
       A = np.float128
       S = np.float128
       A = np.mean(average)
       S = np.std(Std)
            
        
    
    print("Averag is ", A, "Standard Deviation is", S) 
