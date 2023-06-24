Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
L=[10,3.4,8,"d"]
type(L)
<class 'list'>
L[3]
'd'
L.append(100)
L
[10, 3.4, 8, 'd', 100]
L.append(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    L.append(a)
NameError: name 'a' is not defined
L.append("a")
L
[10, 3.4, 8, 'd', 100, 'a']
l.[1,2,3,4,5,6,7,'holiday']
SyntaxError: invalid syntax
L=[1,2,3,4,5,6,7,'holiday']
L
[1, 2, 3, 4, 5, 6, 7, 'holiday']
L.append(9)
L
[1, 2, 3, 4, 5, 6, 7, 'holiday', 9]
L.extend([100,200,300])
L
[1, 2, 3, 4, 5, 6, 7, 'holiday', 9, 100, 200, 300]
L.insert(8,'sam')
L
[1, 2, 3, 4, 5, 6, 7, 'holiday', 'sam', 9, 100, 200, 300]
L.remove('holiday')
L
[1, 2, 3, 4, 5, 6, 7, 'sam', 9, 100, 200, 300]
L.pop(300)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    L.pop(300)
IndexError: pop index out of range
L.pop(9)
100
L
[1, 2, 3, 4, 5, 6, 7, 'sam', 9, 200, 300]
L.remove(2)
L
[1, 3, 4, 5, 6, 7, 'sam', 9, 200, 300]
L.index(7)
5
L.index(1)
0
L.count(1)
1
L.sort()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    L.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
L.remove('sam')
L
[1, 3, 4, 5, 6, 7, 9, 200, 300]
L.sort()
L
[1, 3, 4, 5, 6, 7, 9, 200, 300]
L.copy()
[1, 3, 4, 5, 6, 7, 9, 200, 300]
L.copy(1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    L.copy(1)
TypeError: list.copy() takes no arguments (1 given)
L.copy()
[1, 3, 4, 5, 6, 7, 9, 200, 300]
x=L.copy()
x
[1, 3, 4, 5, 6, 7, 9, 200, 300]
