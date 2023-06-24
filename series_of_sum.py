'''n=int(input("Enter the number"))
s=0.0
for i in range(1, n+1):
    a=1.0/i
    s+=a
print(s)'''

#wacp to take a 3digit input like n=123
#and print in reverese order
'''n=int(input())
while n!=0:
    rem=n%10
    print(rem,end="")
    n=n//10'''

#strong or not
'''n=int(input())
a=0
for i in range(1,n):
    if (n%i==0):
        #a+=i
        if a==n:
            print("Strong")
        else:
            print("Not strong")'''

#counting the alphabets
'''s=input()
i=c=1
while i<len(s):
    if s[i]==s[i-1]:
        c+=1
    else:
        print(s[i-1], end="")
        print(c,end="")
        c=1
    i+=1
print(s[i-1], end="")
print(c)'''
#
s1=input()
s2=input()
if(s2.isupper()):
    s1=s1.replace(s2,chr(ord(s2)+32))
else:
    s1=s1.replace(s2,chr(ord(s2)-32))
print(s1)

    
        

















