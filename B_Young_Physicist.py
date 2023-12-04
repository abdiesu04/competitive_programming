n=int(input())

costs=list(map(int,input().split()))
cum=[costs[0]]
for i in range(1,n):
    cum.append(costs[i]+cum[i-1])

    
costs.sort()
cumsort=[costs[0]]
for i in range(1,n):
    cumsort.append(costs[i]+cumsort[i-1])
    
    
m=int(input())
arr=[]
for i in range(m):
    arr.append(list(map(int,input().split())))


for i in arr:
    a=i[0]
    b=i[1]-1
    c=i[2]-1
    if a==1:
        if b==0 : print(cum[c])
        else: print(cum[c]-cum[b-1])
    else:
        if b==0:print(cumsort[c])
        else:print(cumsort[c]-cumsort[b-1])
 

       