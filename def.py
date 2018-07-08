Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> a,b=b,a
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> a=10
>>> b=20
>>> a,b=b,a
>>> 
>>> 
>>> 
>>> 
>>> ptint(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ptint(a)
NameError: name 'ptint' is not defined
>>> a=
SyntaxError: invalid syntax
>>> print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a)?
>>> print(a)
20
>>> 
=============================== RESTART: Shell ===============================
>>> str= 'hello'
>>> print(str)
hello
>>> 
>>> 
>>> a=10
>>> b=20
>>> c=a+b
>>> print(c)
30
>>> a=10
>>> c=a*a
>>> print(c)
100
>>> 
>>> 
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print(a)
20
>>> print(b)
10
>>> 
>>> a=[2,5,5,6]
>>> reverse(a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    reverse(a)
NameError: name 'reverse' is not defined
>>> str=[raw_input('Enter number') for i in range(5)}
SyntaxError: invalid syntax
>>> str=[raw_input('Enter number') for i in range(5)]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    str=[raw_input('Enter number') for i in range(5)]
  File "<pyshell#42>", line 1, in <listcomp>
    str=[raw_input('Enter number') for i in range(5)]
NameError: name 'raw_input' is not defined
>>> str=[input('Enter number') for i in range(5)}
SyntaxError: invalid syntax
>>> str=[int(input('Enter number')) for i in range(5)]
Enter number1
Enter number2
Enter number3
Enter number4
Enter number5
>>> print(str)
[1, 2, 3, 4, 5]
>>> def get_res(branch,**subs)
SyntaxError: invalid syntax
>>> def get_res(branch,**subs):
	total=0
	for k,v in sub.items():
		if branch== "cse" and
		
SyntaxError: invalid syntax
>>> def get_res(branch,**subs):
	total=0
	for k,v in sub.items():
		if branch== "cse" and k in['c','java']:
			total+=v
	return total
sub={'c',20,'java'}
SyntaxError: invalid syntax
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
Traceback (most recent call last):
  File "C:/Users/HRUSHI/Desktop/mutex/def.py", line 7, in <module>
    total=get_result('cse','sub')
NameError: name 'get_result' is not defined
>>> 
Traceback (most recent call last):
  File "C:/Users/HRUSHI/Desktop/mutex/def.py", line 7, in <module>
    total=get_result('cse','sub')
NameError: name 'get_result' is not defined
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
Traceback (most recent call last):
  File "C:/Users/HRUSHI/Desktop/mutex/def.py", line 7, in <module>
    total=get_res('cse','sub')
TypeError: get_res() takes 1 positional argument but 2 were given
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
Traceback (most recent call last):
  File "C:/Users/HRUSHI/Desktop/mutex/def.py", line 7, in <module>
    total=get_res('cse','sub')
  File "C:/Users/HRUSHI/Desktop/mutex/def.py", line 3, in get_res
    for k,v in sub.items():
NameError: name 'sub' is not defined
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
40
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
40 marks
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
40
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
40
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
45
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
0
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
20
>>> 
=============== RESTART: C:/Users/HRUSHI/Desktop/mutex/def.py ===============
20
>>> 
