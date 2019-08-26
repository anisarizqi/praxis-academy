def call(x, f):
	return f(x)

square = lambda x : x*x
increament = lambda x : x+1
cube = lambda x : x*x*x
decrement = lambda x : x-1
funcs = [square, increament, cube, decrement]

from functools import reduce
print(reduce(call, funcs, 96))