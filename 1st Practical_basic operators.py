Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 100
type(x)
<class 'int'>
x = "hello"
type(x)
<class 'str'>
x= 3.14
type(x)
<class 'float'>
x = i + 1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x = i + 1
NameError: name 'i' is not defined. Did you mean: 'id'?
x = ["apple", "banana" , "fruit" ]
type(x)
<class 'list'>
range(x)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    range(x)
TypeError: 'list' object cannot be interpreted as an integer
x = {"apple", "banana" }
type(x)
<class 'set'>
x = ("apple", "banana")
type(X)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
range(x)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    range(x)
TypeError: 'tuple' object cannot be interpreted as an integer
x = ("apple","banana")
type(x)
<class 'tuple'>
x = {("banana","apple")}
type(x)
<class 'set'>
x = frozenset{"apple","banana"}
SyntaxError: invalid syntax
x = frozenset{("apple","banana")}
SyntaxError: invalid syntax
x = frozenset([("apple", "banana")])
type(x)
<class 'frozenset'>
x = ["10", "20", "30"]
x.append(40)
print(x)
['10', '20', '30', 40]
print (x(2))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print (x(2))
TypeError: 'list' object is not callable
x(2)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x(2)
TypeError: 'list' object is not callable
print x(2)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print (x[2])
30
y = ("21,"22","45")
     
SyntaxError: unterminated string literal (detected at line 1)
y = (21,45,88)
     
x = ("apple","banana")
     
x.append(90)
     
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x.append(90)
AttributeError: 'tuple' object has no attribute 'append'


#operators --------------
     
#arthemactic operator
     
x = 1 + 6
     
print(x)
     
7
x = 68 - 45
     
print(x)
     
23
x = 45/5
     
print(X)
     
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
     
9.0
x = 56*89
     
print(x)
     
4984
x = 89%7
     
print(x)
     
5
x = 87**78
     
print(x)
     
19164685832994576242645010005695679285565305688749352887845166294156669748766857458943278384895921951673431724372964727565938773303631034547472370681329
x = 34//3
     
print(x)
     
11

#assignment operator
     
x = 97
     
x =x + 34
     
print(x)
     
131
x = x -90
     
print(x)
     
41
x = x /2
     
print(x)
     
20.5
x = x // 3
     
print(x)
     
6.0
x =x % 5
     
print(x)
     
1.0
x =x **9
     
print(x)
     
1.0

#comparison operator
     
x = 9
     
y = 10
     
x == y
...      
False
>>> x != y
...      
True
>>> x > y
...      
False
>>> x < y
...      
True
>>> X =< y
...      
SyntaxError: invalid syntax
>>> x <= y
...      
True
>>> x >= y
...      
False
>>> 
>>> #logical operator
...      
>>> x = 7
...      
>>> y = 8
...      
>>> x && y
...      
SyntaxError: invalid syntax
>>> x > y and x < y
...      
False
>>> x > y or x< y
...      
True
>>> 
>>> #identity operator
...      
