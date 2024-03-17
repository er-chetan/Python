def gen(x):
    for i in range(3,x):
        yield i
len=gen(7)
# print(len(le))
# l=list(le)
print(type(len))
print(next(len))
print(next(len))  
print(next(len))  
print(next(len))  
print(next(len))  

# for i in le:
#     print(i)
