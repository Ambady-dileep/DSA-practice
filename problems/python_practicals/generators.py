def func(a):
    for i in a:
        yield i

a = [1,2,3,4,5]

gen = func(a)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
