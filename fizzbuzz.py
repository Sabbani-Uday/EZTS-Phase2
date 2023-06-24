'''n=int(input())
if(n%15==0):
    print("FIZZBUZZ")
elif(n%5==0):
    print("FIZZ")
elif(n%3==0):
    print("BUZZ")'''

#given an array sort the array in correct order
'''a=[0,1,1,0,0,1,1,0,0 ]
l1=[]
l2=[]
for i in a:
    if i==0:
        l1.append(i)
    elif i==1:
        l2.append(i)
print(l1+l2)'''
#given an array size n where every number appear twice
#except one number find that number....
#a=[3,1,5,5,3,3,5,3,2,2]

#given two sorted array a and b print in merge and
#sorted array
a=[-4,-2,1,3,7,9,10]
b=[-1,5,11]
c=a+b
c.sort()
print(c)
