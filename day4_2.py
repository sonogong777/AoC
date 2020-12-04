#!/usr/local/bin/python3

import sys
import re

key_list=['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:'] 

valid_passport=0          
valid_field=0
keycount=0

#convert list to dictionary when they are in order
def convertList(myList):
    new_dict={}
    new_dict = { myList[i]: myList[i+1] for i in range(0, len(myList), 2) }  #using lambda
    return new_dict

def checkData(myDict):
    test=0
    eye_color=['amb','blu','brn','gry','grn','hzl','oth']
    
    if int(myDict['byr']) >= 1920 and int(myDict['byr']) <= 2002 \
    and int(myDict['iyr']) >= 2010 and int(myDict['iyr']) <= 2020 \
    and int(myDict['eyr']) >= 2020 and int(myDict['eyr']) <= 2030 \
    and len(myDict['pid']) == 9 \
    and myDict['ecl'] in eye_color:
        test+=5
        
    if myDict['hcl'][0] == '#' and len(myDict['hcl']) == 7:
        char_test=0
        for char in myDict['hcl'][1:]:
            if char.isnumeric() or char in 'abcdef':
                char_test+=1
        if char_test == 6:
            test+=1
        
    if 'cm' in myDict['hgt']:
        height=int(re.sub("[^0-9]", "", myDict['hgt']))
        if height >= 150 and height <= 193:
            test+=1
    if 'in' in myDict['hgt']:
        height=int(re.sub("[^0-9]", "", myDict['hgt']))
        if height >= 59 and height <= 76:
            test+=1

    if test == 7:
        valid=1
    else:
        valid=0

    return valid


try:
    with open('day4.input', 'r') as input_file:
        all_data=input_file.read()
        pp_data=all_data.split('\n\n')  #catch the empty lien

except IOError:
    print("Something went wrong when attempting to read file.")
    

for data_item in pp_data:
    keycount=0
    for key in key_list:
        if key in data_item:
            keycount+=1
    if keycount >= 7:
        valid_field+=1
        temp_list=[]
        temp_list=re.split(r'[:,\s]',data_item)
        if len(temp_list)%2:
            temp_list.pop()
        valid_passport+=checkData(convertList(temp_list)) #work with the dict while we have the small number of data set
        
    
print('valid passport: ',valid_passport)
print('data with values',valid_field)