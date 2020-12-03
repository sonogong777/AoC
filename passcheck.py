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
    
    if pattern_count >= start_range and pattern_count <= end_range:
        print(pattern, start_range, end_range, test_string, pattern_count)
        count+=1
        
print(count)
        
   # if len(test_string) >= start_range and len(test_string) <= end_range:
        
   #     print(pattern_range,test_string,len(test_string))
        
    #rint(len(string))