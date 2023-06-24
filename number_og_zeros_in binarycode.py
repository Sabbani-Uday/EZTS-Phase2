'''n=int(input("Enter number"))
c=0
while((1&n)!=1):
    c=c+1
    n=n>>1'''

#given a number n print no.of divisors/Factors  in n?
n=int(input("Enter number"))
i=1
c=0
while(i<=n/i):
    if(n%i==0):
        print(i,end=" ")
        if(i==n/i):
            c+=1
        else:
            c+=2
print(c)



#given an array of size n every number
#is repeated twise print that number
l=[8,5,8,3,1,5,3,1,9]
z=0
for i in range(len(l)):
    z=z^l[i]
print(z)
    
