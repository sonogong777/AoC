#!/usr/bin/python3

import sys
import string

num_list=[]
file=open('passinput.txt','r')

count=0
for line in file:
    line_list=line.split()
    pattern_range=line_list[0].split(sep="-")
    start_range=int(pattern_range[0])
    end_range=int(pattern_range[1])
    pattern=line_list[1].strip(":")
    test_string=line_list[2].strip("\n")
    pattern_count=test_string.count(pattern)
    
    valid=0
    # pattern count within start_range and end_range
    #remove from the previous..
    #if pattern_count >= start_range and pattern_count <= end_range:
    if pattern in test_string[start_range-1]:
        valid+=1
        print(start_range,test_string[start_range-1],test_string)
        
    if pattern in test_string[end_range-1]:
        valid+=1
        print(end_range,test_string[end_range-1],test_string)
    
    if valid == 1:
        count+=1
        print(valid,count)


 
print(count)