#!/usr/local/bin/python3
import sys
import os

a2d_list = []
#open file and read in line by line and strip the \n 
try:
    with open('input3.txt', 'r') as current_file:
        for line in current_file.readlines():
                a2d_list.append(line.strip('\n'))
except IOError:
    print("Something went wrong when attempting to read file.")

#function to identify the tree in the slope down/right.

def findTree():
    count=0
    move_right=3
    start_column=0
    for lines in a2d_list:    
        if start_column > len(lines)-1:
            start_column=start_column-len(lines)
        if lines[start_column] == "#":
            count+=1
        start_column+=move_right
    print(count)

findTree()