n=int(input())
for i in range(1,n+1):
    for j in range(n+1-i):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    for j in range(i-1):
        print("*",end='')
    print()printing pattern 1
