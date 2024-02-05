import sys
l = []
for _ in range(int(sys.stdin.readline())):
    n = int(input())
    
    if n != 0:
        l.append(n)
    else:
        l.pop(-1)
        

print(sum(l))