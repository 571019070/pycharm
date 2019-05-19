def add(a, b):
    return a+b

print(add(10, 90))

f = lambda a,b : a+b
print(f(10,20))
print((lambda a, b : a+b) (10,20))