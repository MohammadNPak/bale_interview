k = int(input())
n = int(input())
a = tuple(map(int,input().split()))

for i,ai in enumerate(a):
    for j,aj in enumerate(a[i:]):
        if ai+aj==k:
            print(ai,aj)
            b=1
            break 
    if b:
        break
