'''for i in range(5):
    for j in range(5-i-1):
        print(" ",end="")
    for k in range(2*i-1):
        print("* ",end="")
    print()'''

'''n=4
for i in range(n+1):
    for j in range(n-i):
        print(' ',end="")
    x=1
    for j in range(1,i+1):
        print(x,'',sep="",end="")
        x=x*(i-j)//j
    print()'''

'''n=int(input("enter rows"))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()'''

'''i=1
while(i<=rows):
    j=1
    while(j<=i):
        print(number,end="")
        number=number+1
        j=j+1
    i=i+1
    print()'''

for i in range(1,5):
    for j in range(1,5):
        if i==j or j==1 or i==4:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    

















