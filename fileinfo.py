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

######
#质因数分解.py
'''
x=int(input())
i=2
a=''
    
while x%i==0 and x>=i:
    
    a=a+str(i)+' * '
    x=x/i

else:
    i+=1
    a=''
    a=a+str(i)+' * '
    x=x/i
print(a)
'''

###质因数分解

import math
number=int(input())
list=[]
def getChildren(num):
    print('*'*30)
    isZhishu=True
    i=2
    square=int(math.sqrt(num))+1
    while i<=square:
        if num%i==0:
            list.append(i)
            isZhishu=False
            getChildren(num/i)
            i+=1
            break
        i+=1
    if isZhishu:
        list.append(num)
getChildren(number)
print(list)

