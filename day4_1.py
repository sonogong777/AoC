#!/usr/local/bin/python3

import sys

key_list=['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:'] 
          
valid_passport=0
keycount=0

try:
    with open('day4.input', 'r') as input_file:
        all_data=input_file.read()
        pp_data=all_data.split('\n\n')  #catch the empty lien
                
except IOError:
    print("Something went wrong when attempting to read file.")

for data in pp_data:
    keycount=0
    for key in key_list:
        if key in data:
            keycount+=1
    if keycount >= 7:
        valid_passport+=1

print(valid_passport)
