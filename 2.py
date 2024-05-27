def remove(a):
    s=0
    output = []
    l = len(a)
    x,y = -1,-1
    for i,row in enumerate(a):
        for j,col in enumerate(a[i]):
            if a[i][j]>=0:
                y=i
                x=j
                break
        if x!=-1 or y!=-1:
            break
        
    else:
        return a,0
    
    for k in range(l):
        if k<y:
            output.append(a[k][:])
        else:
            t = a[k][:x]
            s+=len(a[k])-len(t)
            if t:
                output.append(t)
                        
    return output,s

n = int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

result = 0
a,s = remove(a)
result+=s
while s!=0:
    a,s=remove(a)
    result +=s
print(result)
print(a)


