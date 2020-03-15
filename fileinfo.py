a,b=map(int,input().split())
ls=[]
A=1
for i in range(a,b+1):
    k=int(pow((i+1),0.5))
    for j in range(2,k+1):
        if i%j==0:
            A=0
            break
    if A==1:
        ls.append(i)
    A=1
c=int(sum(ls))
print(c)

#####
a,b=map(int,input().split())
ls=[]
A=1
for i in range(a,b+1):
    k=int(pow((i+1),0.5))
    for j in range(2,k+1):
        if i%j==0:
            A=0
            break
    if A==1:
        ls.append(i)
    A=1
c=int(sum(ls))
print(c)