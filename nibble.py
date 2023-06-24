'''#calculate the nibble value of b>>+2
n=int(input("enter the value"))
s=0.0
for i in range(1,n+1):
    a=1.0/(i**2)
    s=s+a
print(s)

#

for i in range(1,11):
    if i==5:
        continue
    print(i,end=" ")
print("over")

#
str='jamesbond007'
print(str.island())
'''
num=int(input("Enter the term"))
if num%2==0:
    num=num//2
    print(7**(num-1))
else:
    num=num//2+1
    print(6**(num-1))


