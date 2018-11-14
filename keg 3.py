Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Sufyan Habib Zaini"
>>> NIM = "L200184098"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Because the "X" data has changed to integer data type
>>> type(b)
<class 'int'>
>>> # Because the "Nama" data has a "len" instruction
>>> a / b
61.0
>>> # Because the result of 1092 divided by 23 is 61.0
>>> a // b
61
>>> # Because the meaning of "//" is division with rounding down
>>> 10 * (a - 999)
990
>>> # Because the value of "a" minus 999 is 93, after that it will multiplied by 10 and the result is 990
>>> b ** 2
324
>>> # Because the meaning of "**" is square
>>> a % b
0
>>> # Because the meaning of "%" is remaining of the result
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Because "12.5" is a decimal number
>>> a / c
87.84
>>> # Because the result of 1092 divided by 12.5 is 87.36
>>> a // c
87.0
>>> # Because the meaning of "//" is division with rounding down and the operand type is writed in decimal number
>>> a % c
10.5
>>> # Because the meaning of "%" is remaining of the result
>>> c > b
False
>>> # Because the "b" data has a bigger value than the "c" data
>>> type(c > b)
<class 'bool'>
>>> # Because "True" or "False" is a boolean data type
>>> a > b and b > c
True
>>> # Because in "and" operator symbol, if "True" meet with "True", The result is "True"
>>> a > 1100 or b < 10
False
>>> # Because in "or" operator symbol, if "False" meet with "False", The result is "False"
>>> 
