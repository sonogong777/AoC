#!/usr/local/bin/python3
input_file = open("day7.input")
input_text = input_file.read()

counter=0
for line in input_text:
    print(line)
    if 'shiny gold bags,' in line or 'shiny gold bags' in line:
        counter += 1
        

print(counter)