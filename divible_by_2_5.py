x=int(input("List SIZE"))
l=[]
sum=0
for i in range(x):
    n=int(input("enter elements"))
    l.append(n)
    sum=sum+n
print(l)
print("sum:",sum)
if(sum%2==0 and sum%5==0):
    print("divislible by 2 5")
else:
    print("not divisible")
