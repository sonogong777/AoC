#!/usr/local/bin/python3
f = open("input3.txt", "r")

lists = []
h = ""

for i in f:
    h = i.replace("\n", "")
    lists.append(h)

def finder(right,down):
    hits = 0
    upBy = 0
    for i in lists[::down]:
       # print(hits,upBy)
        if upBy > len(i)-1:
            upBy = upBy - 31
        if i[upBy] == "#":
            hits = hits + 1
        upBy = upBy + right
    print(hits)
    return hits

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

answer=[]
answer.append(finder(1,1))
answer.append(finder(3,1))
answer.append(finder(5,1))
answer.append(finder(7,1))
answer.append(finder(1,2))
print(answer)
print(multiplyList(answer))

