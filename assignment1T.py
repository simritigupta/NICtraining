# -*- coding: utf-8 -*-
"""
Created on Sat May 25 14:30:50 2019

@author: SIMRITI
"""

#question 1 of assignment 1
def server_utilization(cpu,ram,Num_VMs):
    
    utilization=(0.5*Num_VMs*0.2+ 0.2*Num_VMs*0.4)/(0.35*cpu + 0.65*ram)*100
    return(utilization)
    
print("server 1","  ",(server_utilization(2,4,5)))
print("server 2","  ",server_utilization(2,2,3))
print("server 3","  ",server_utilization(4,4,10))
print("server 4","  ",server_utilization(3,6,12))
print("server 5","  ",server_utilization(5,10,20))

# question 2 for assignment 1 taking input from the user
def server_utilization1(cpu,ram,Num_VMs):
   
    utilization=(0.5*Num_VMs*0.2+ 0.2*Num_VMs*0.4)/(0.35*cpu + 0.65*ram)*100
    return(utilization)
    
for i in range(1,6):
    cpu=int(input("Enter the number of cpu used:"))
    ram=int(input("Enter the ram:"))
    Num_VMs=int(input("Enter the number of virtual machines used:"))
    print("server"+ str(i)," ",server_utilization(cpu,ram,Num_VMs))   
print("assignment1 done")    
    
