k = int(input())
n = int(input())
a = tuple(map(int,input().split()))

data={}
for i,ai in enumerate(a):
    complement = k-ai
    if complement in data:
        print("Yes") 
        break
    else:
        data[ai] = complement
else:
    print("No")