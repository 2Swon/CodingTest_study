N = input()
ans = ''
for i in N:
    if i.islower():
       ans += i.upper()

    else:
        ans += i.lower()

print(ans)