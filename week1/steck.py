#	1.3	Функции и стек вызовов
print('~~~~СТЭК вызовов~~~~~')

def g():
	print('I am func g')

def f():
	print('I am func f')
	g()
	print('I am func f')

print('I am outside of any func')
f()
print('I am ounside of any func')

#~~~~СТЭК вызовов~~ex.2~~~
x = [1, 2, 3]
x.append(4)
x.append(5)

print(x)
top = x.pop()
print(top)
print(x)

top = x.pop()
print(top)
print(x)


#~~~~СТЭК вызовов~~ex.3~~~
def dev(a, b):
	return a / b
	
print(dev(10,3))


print(dev(2,4) is None)
