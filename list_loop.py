l=[n for n in range(150,181)]
print(l)
#even=[]
#odd=[]
even=[e for e in l if(e%2==0)]
print("even",even)
odd=[o for o in l if(o%2!=0)]
print("odd",odd)

********************

l=[i for i in range(1,11)]
print(l)
l1=["even" if i%2==0 else "odd" for i in l]
print(l1)


