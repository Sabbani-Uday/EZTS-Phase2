#general syntax to create class
#obj_name=class_name()
'''class abc:
    var=10
    def display(self):
        print("this is in class method")
obj=abc()
print(obj.var)
obj.display()'''

#constructor class
'''class abc():

    def __init__(self,val):
        self.val=val
        print("the value is",val)
obj=abc(110)'''

#program to check even or odd
'''class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"Even")
        else:
            print(num,"Odd")
n=number()
n.even_odd(99)'''

#write a program

 
#output:
 #   even number are:[32,54]
  #  odd number are:[21,43,65]'''
'''class number:
    evens=[]
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.evens.append(num)
        else:
            number.odds.append(num)

n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print("Even numbers are:",number.evens)
print("odd numbers are:",number.odds)'''

#write a prog class circle use the class variable
#to define constant pi=3.14 use the class variable
#to calculate the area and circumference in different
#functions with radius 7.5
'''class circle:
    def ac(self,radius):
        pi=3.14159
        print("Circumference of the circle is",2*pi*(radius))
        print("radius of the circle is",pi*((radius)**2))
object=circle()
print(object.ac(4))'''


class circle():
    pi=3.14159
    def area(self,radius):
        a=self.pi*radius**2
        print("Area=",a)
    def circum(self,radius):
        c=2*self.pi*radius
        print("Cir=",c)
radius=circle()
radius.area(7.5)
radius.circum(7.5)


1.__del__() deletes the scope autom...
2.__repr__() string representation..
3.__cmp__() compare two objects..
4.__len__() length of the class objects..
5.__call__() the method lets a class to act like a function
6.__it__,__le__,__eq__,__ne__,__gt__,__ge__ these are used to compare 2objecta
7.__hash__  it is used to hash the objects
8.__iter__ iterrates over the objects
9.__getitem__ used for indexing
10.def __grtitem()
11.__setitem__()
12.def __setitem__(self,key,value)

 






















































