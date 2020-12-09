#!/usr/local/bin/python3

def getDup(listOfElems):
    ''' Get frequency count of duplicate elements in the given list '''
    dictOfElems = dict()
    # Iterate over each element in list
    for elem in listOfElems:
        # If element exists in dict then increment its value else add it in dict
        # remove \n from the list
        if elem == '\n':
            continue
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
    dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
    # Returns a dict of duplicate elements and thier frequency count
    return dictOfElems

try:
    with open('day6.input', 'r') as input_file:
        all_data=input_file.read()
        answer_data=all_data.split('\n\n')  #catch  empty lien
                
except IOError:
    print("Something went wrong when attempting to read file.")

counter=0
group=0
for answers in answer_data:
    #remove trailing \n
    test=answers.rstrip("\n")
    person=test.count('\n')+1

    #if person > 1:
    tempDict=getDup(test)
    
    for key in tempDict:
        if tempDict[key] == person:
            counter+=1
    group+=1
    print(group,counter)
    
print(counter)
