a = 5
print(type(a), id(a))
print(isinstance (a, int))

a = 'hello'
print(type(a), id(a))
a = 42.0 * 3.1415926
print(type(a), id(a))

data = 3.14
print(isinstance (data, (int, float, complex)))
data = 'd'
print(isinstance (data, int))

num = 2 + 2 * 2
digit = 36 / 6
print (num == digit)
print (num is digit)


txt = 'Hello world!'
print (txt, id (txt))
txt = txt.replace (' ', '_')
print (txt, id(txt))
