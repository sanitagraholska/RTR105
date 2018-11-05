Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> str1 = "Hello"
>>> str2 = 'there'
>>> bob = str1 +str2
>>> print(bob)
Hellothere
>>> str3 = '123'
>>> str3 = str3 +1

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str3 = str3 +1
TypeError: cannot concatenate 'str' and 'int' objects
>>> x = int(str3) +1
>>> print(x)
124
>>> '''
'''
'\n'
>>> 
>>> 
>>> name = input('Enter:'°
	     
SyntaxError: invalid syntax
>>> name = input ('Enter:')
Enter:Chuck

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name = input ('Enter:')
  File "<string>", line 1, in <module>
NameError: name 'Chuck' is not defined
>>> print(name)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
>>> x=int(apple)-10

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x=int(apple)-10
NameError: name 'apple' is not defined
>>> fruit = 'banana'
>>> letter = fruit [1]
>>> print(letter)
a
>>> x=3
>>> w = fruit [x-1]
>>> print(w)
n
>>> zot = 'abc'
>>> print(zot[5])

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(zot[5])
IndexError: string index out of range
>>> fruit = 'banana'
>>> print(len(fruit))
6
>>> s = 'Monty Phyton'
\
>>> print(s[0:4])
Mont
>>> print(s[6:7])
P
>>> print(s[6:20])
Phyton
>>> s= 'Monty Phyton'
>>> print(s[:2])
Mo
>>> print(s[8:])
yton
>>> print(s[:])
Monty Phyton
>>> a= 'Hello'
>>> b= a+ 'There'
>>> print(b)
HelloThere
>>> c= a+ '' + 'There'
>>> print(c)
HelloThere
>>> fruit = 'banana'
\
>>> 'n''in fruit
SyntaxError: EOL while scanning string literal
>>> greet='Hello Bob'
>>> zap= greet.lower()
>>> print(zap)
hello bob
>>> print(greet)
Hello Bob
\
>>> print('Hi There'.lower())
hi there
>>> stuff= 'Hello world'
>>> type(stuff)
<type 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> fruit = 'banana'
>>> pos = fruit.find('na'°
		 
SyntaxError: invalid syntax
>>> pos = fruit.find('na')
>>> print(pos)
2
>>> aa=fruit.find('z')
>>> print(aa)
-1
>>> greet = 'Hello Bob'
>>> nnn = greet.upper()
>>> print(nnn)
HELLO BOB
>>> www=greet.lower()
>>> print(www)
hello bob
>>> greet = 'Hello Bob'
>>> nstr = greet.replace('Bob''Jane')

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    nstr = greet.replace('Bob''Jane')
TypeError: replace() takes at least 2 arguments (1 given)
>>> nstr = greet.replace('Bob','Jane')
>>> print(nstr)
Hello Jane
>>> nstr=greet.replace('o','X')
>>> print(nstr)
HellX BXb
>>> greet ='  Hello Bob '
>>> greet.lstrip()
'Hello Bob '
>>> greet.rstrip()
'  Hello Bob'
>>> greet.strip()
'Hello Bob'
>>> line='Please have a nice day'
>>> line.startswith('Please'°
		
SyntaxError: invalid syntax
>>> line.startswith('Please')
True
>>> line.startswith('p')
False
>>> 

