x=int(input("enter 1st value"))
y=int(input("enter 2nd value"))
z=int(input("enter 3rd value"))
avg=(x+y+z)/3
if(avg>75):
    print("happy")
elif(avg<75):
    print("jolly")



#*****************

x=int(input("enter any value"))
if(x%2==0 and x>0):
    print("positive even")
elif(x%2==0 and x<0):
    print("negative even")
elif(x%2!=0 and x>0):
    print("positive odd")
elif(x%2!=0 and x<0):
    print("negative odd")
