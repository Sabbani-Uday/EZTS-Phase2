#greatest of three numbers
'''n1=int(input("enter 1st number"))
n2=int(input("enter 2st number"))
n3=int(input("enter 3st number"))
if(n1>n2 and n1>n3):
    print(n1,"is greater")
elif(n2>n1 and n2>n3):
    print(n2,"is grater")
else:
    print(n3,"is greater")'''

'''#Given number is prime or not
n=int(input("Enter any number"))
if(n>1):
    for i in range(2,int((n/2)+1)):
                   if(n % i==0):
                       print(n,"is not prime")
                   else:
                       print(n,"is prime")'''

def multiply():
    x=int(input("enter number"))
    p=1
    for i in range(11):
        p=x*i
        print(x,"*",i,"=",p)
multiply()


                    
                   
                

