## 17-12-2023

# 1.) iterator tools
# 2.) can i convert a dictionary into list if yes then the output is??
# 
# 


d={'name':'chetan','place':'ambala'} 

# print(d.items())
# print(d.keys())
# print(d.values())


# for i in d.keys():
#     print(i)

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)


# for i,j in d.items():
#     print(i,"=",j)

# for i in d.items():
#     for j in range(len(i)):
#         if j ==0:
#             print("key = ",i[j], end=", ")
#         elif j==1:
#             print("Value = ", i[j])





w = {"hempen" : "1. Made of hemp; as, a hempen cord. 2. Like hemp. \"Beat into a hempen state.\" Cook."}

# for i in w.values():
#     print(i.split('. '))



a= [1,2,4,5,23,34,45,56,67,577]
print(a)

li = a
print(li)

li[2] = 999

print(li)
print(a)

a= [1,2,4,5,23,34,45,56,67,577]
print(a)

li1 = a.copy()
print(li1)

li1[2] = 999

print(li1)
print(a)
