#!/usr/bin/python3

import sys

num_list=[]
file=open('expense.txt','r')
for line in file:
  num_list.append(line)

for j in range(0,len(num_list)):
   for k in range(0,len(num_list)):
       for l in range(0,len(num_list)):
            total=int(num_list[j])+int(num_list[k])+int(num_list[l])
            if total == 2020:
                print(num_list[j],num_list[k],num_list[l])    
                print(int(num_list[j])*int(num_list[k])*int(num_list[l]))
    
