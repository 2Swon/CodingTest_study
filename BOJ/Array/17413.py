import sys

str = list(sys.stdin.readline().rstrip())
i=0
start=0
while i < len(str):
    
    if str[i] == "<":
        i= i+1
        while str[i] !=">":
            i= i+1
        i= i+1
    
    elif str[i].isalnum():
        start = i
        while i < len(str) and str[i].isalnum() :
            i= i+1
        
        temp = str[start:i]
        temp.reverse()
        str[start:i] = temp
        
    else:
        i= i+1
        

print("".join(str))