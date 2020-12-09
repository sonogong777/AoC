#!/usr/local/bin/python3

import sys
          

try:
    with open('day6.input', 'r') as input_file:
        all_data=input_file.read()
        answer_data=all_data.split('\n\n')  #catch  empty lien
                
except IOError:
    print("Something went wrong when attempting to read file.")

#remove \n in element
answer_list= [element.replace('\n', '') for element in answer_data]

counter=0
for answers in answer_list:
    list=set(answers)
    counter+=len(list)

print(counter)