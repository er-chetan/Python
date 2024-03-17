##########-------collection--------##########

#############--------tuple---------##########

##########--------- this is a tuple structuring --------#########
# a=(1,2,3,4,5)
# print(type(a))
# print(a) 

###-----write also without bracket----#####

# b=1,2,3,4,5
# print(b)

##########--------- this is a tuple distructuring --------#########

# a,b=2,3

# print(a)
# print(b)

###### access the element w.r.t to variable in tuple-----#####

# a=(1,2,3,4,5)
# p,q,r,s,t=a

# print(r)

####----to copy from a to b-----#####

# a=(1,2,3,4,5)
# b=a
# print(b)

##########---------- methods in tuple -----########

m=(10,11,12,13,10,14)

# to find the index
# print(m.index(12)) 

# to count the number of repeated element
# print(m.count(10))

#length of the tuple
# print(len(m))

#  to find the minimum
# print(min(m))

# to fint the maximum
# print(max(m))

# to find the sum of elements
# print(sum(m))

# to delete the tuple
# print(del(m))  error


#################---------------set----------------###################

A={1,2,3,4,5}
B={1,2,10,11,14,15}
# print(A)

####-----union-------#####
# print(A.union(B))

# by operator
# print(A|B)


#########----------intersection--------##########
# print(A.intersection(B))

# by operator
# print(A&B)

#########----------differnce------##########
# print(A.difference(B))
# print(B.difference(A))

# by operator
# print(A-B)
# print(B-A)

#######-----symmeteric_differnce------########
# print(A.symmetric_difference(B))

# by operator
# print((A-B)|(B-A))

######---- disjoint all the element in sets must be unique------ ########

x={1,2,3,4,5,'shyam','ram'}
y={6,7,8,9}

# print(x.isdisjoint(y))

###########--------- subset ---------#########

z={1,2,3,4}
# print(z.issubset(x))
# print(x.issubset(z))

####-------- insert a new element ---------######

# x.add(23)
# print(x)

########--------- update ---------######### 
# (in set the concept of index is none that means there is no fixed index of each element)

# x.update('aman')
# print(x)

######------ remove a element ------#######3

# x.remove('ram')
# print(x)

# x.remove('sd') it gives the error because the 'sd' is not present in the set
# print(x)

#######----------  discard ---> to also remove an element --------########
# is also remove the element but if element is not present then the program flows the normal flow of code not give an error

# x.discard('sd')
# print(x)
# x.discard('shyam')
# print(x)



###############------------ list ---------------###################

a=[1,2,3,4.5,6.75,'ram','shyam']

# print(a)

# for i in a:
#     print(i)

# for i in range(0,len(a)):
#     print(i,'=',a[i])

li1=[1,2,3]
li2=[4,5,6]

# li3=li1+li2
# print(li3)

####### ----  another way by using extend

# li1.extend(li2)
# print(li1)

#########--- append
# li1.append(5)
# print(li1)

#####---- li2 list append as an element whole list
# li1.append(li2)
# print(li1)

########---- index ,find

# print(li1.index(1))
# print(li1.find(2))// this not in list now

# print(dir([]))

li = [10,10,10]
# print(li.count(10))
li.insert(0,112)
print(li)


li[1] = 4567
print(li)

# li.remove(112)
# print(li)

# li.pop()
# print(li)


# li.reverse()
# print(li)

# li.sort()
# print(li)


li.sort(reverse=True)
print(li)

########### dictionary #########

d={'name':'chetan','place':'ambala'}  ## this dictionary with zero degree (no nesting )
## two part in dctionary --- valuea and keys

### print the values of keys
# print(d['name'])
# print(d['place'])

### dictionary with one degree 

student={'name':{'firstname':'chetan','lastname':'kumar'},'address':{'city':'barara','distt':'ambala'}}
# print(student['address']['city'])
# print(student['address'])

## by another way get method

# print(student.get('name'))
# print(student.keys())
# print(student['name'].keys())

####### to fetch all the values

# print(student.values())

########## to fetch all the key:pair or item from the dictionary

# print(student.items())

##### to update values in dictionary

# student['name'].update({'firstname':'ram'})
# print(student.items())

d={'name':'chetan','place':'ambala'}

# d.update({'name':'jay'})
# print(d.items())

####### to delete the key and value by using key
# print(d.pop('name'))
# d.pop('name')
# print(d)


############ ton delete the last element from the dictionary

# print(d.popitem())
# print(d)