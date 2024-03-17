#1. Write a Python program to sum all the items in a list.

########## code ##########

# li=[1,2,3,4]
# sum=0
# for i in li:
#     sum=sum+i

# print(sum)    

# 2. Write a Python program to multiply all the items in a list.

########## code ##########

# d=list()
# multi=1
# d=[1,2,5]

# for i in d:
#     multi=multi*i

# print(multi)


# 3. Write a Python program to get the largest number from a list.

########## code ##########

# li=[1,5,2,77,4]
# li.sort()
# print(li," ","largest element-->"," ",li[-1])

### second method

# max=li[0]
# for i in li:
#     if(max<i):
#         max=i

# print(max)

# 4. Write a Python program to get the smallest number from a list.

########## code ##########


# li=[1,5,2,77,4]

# min=li[0]
# for i in li:
#     if(min>i):
#         min=i

# print(min)


# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

########## code ##########

# li= ['abc', 'xyz', 'aba', '1221']

# count=0

# for i in li:
#     if(i[0]==i[-1] and len(i)>2):
#         count+=1

# print(count)




# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


##########   code   #############

# li=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# n1,n2=zip(*li)
# n3=list(n1)
# n4=list(n2)
# n4.sort()
# data=list(zip(n3,n4))
# print(data)


### second method

# n1,n2=zip(*li)

# li1=list(sorted(zip(n2,n1)))
# print(li1)

# n3,n4=zip(*li1)
# print(list(zip(n4,n3)))



# 7. Write a Python program to remove duplicates from a list.

##########   code   #############

# a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# b=set(a)
# print(b)



# 8. Write a Python program to check if a list is empty or not.

##########   code   #############

# li=[1]
# if(len(li)==0):
#     print("empty")
# else:
#     print("non empty"," ",len(li))    


# 9. Write a Python program to clone or copy a list.

##########   code   #############

# original=[1,2,3,4,5,6,7,8,9]

# copy=original
# print(copy)


# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

##########   code   #############


# str="The quick brown fox jumps over the lazy dog"

# str1=str.split()
# count=0
# for i in str1:
#     if(len(i)>3):
#         print(i)
#         count+=1

# print(str1)

# print(count)

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

##########   code   #############

# l1=[1, 2, 3, 4, 5,6,7,8]
# l2=[6, 7, 8, 9]

# l3=set(l1)
# l4=set(l2)

# if(l3&l4):
#     print("true"," ",l3&l4)
# else:
#     print("false")    



# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


##########   code   ##########


# li=['Red', 'Green', 'W


# Write a Python program to generate a 3*4*6 3D array whose each element is *.



# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.


##########   code   #########

# num = [7, 8, 120, 25, 44, 20, 27]
# num=[x for x in num if x % 2 != 0]
# print(num)



# 15. Write a Python program to shuffle and print a specified list.


############# code ###########

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# c=set(color)
# print(c)


# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).


##### code ########
# li=list()

# for i in range(1,31):
    
#     num=i*i
#     li.append(num)


# print(li[0:5],"  ",li[-5:])



# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False

# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

###### code ##########

# li=[3, 5, 7, 13,22]
# count=0
# for i in li:
#     if(i==1):
#         count=1
#         break
#     for j in range(2,i):
#         if(i%j==0):
#             count=1
#             break
#     if(count==1):
#         break

# if(count==0):
#     print("true")
# else:
#     print("false")    

#  Write a Python program to generate all permutations of a list in Python.

# import itertools

# li=list(itertools.permutations([1,2,3]))
# print(li)
# print(len(li))    

# 19. Write a Python program to calculate the difference between the two lists

########## code ###############

# A=[1,3,5,7,9]
# B=[1,2,4,6,7,8] 

# Aset=set(A)
# Bset=set(B)

# C=list((Aset-Bset)|(Bset-Aset))

# print(C)



# 20. Write a Python program to access the index of a list.

########## code ########

# li=[5, 15, 35, 8, 98]

# for i in range(0,len(li)):
#     print(i,li[i])

# 21. Write a Python program to convert a list of characters into a string.  

########## code ########

# li=['p','y','t','h','o','n']
# str=""
# for i in li:
#     str=str+i

# print(str)

###### second method

# str1="".join(li)
# print(str1)


# 22. Write a Python program to find the index of an item in a specified list

######## code ########

# li=[1,33,23,21,56]
# print(li.index(56))


# 23. Write a Python program to flatten a shallow list.

########## code #########

# import itertools

# li=[[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# new_li=list(itertools.chain(*li))
# print(new_li)


# 24. Write a Python program to append a list to the second list.

# li1=[1,2,3,4]

# li2=["red","blue","black"]
# li1.extend(li2)
# print(li1)

# Write a Python program to select an item randomly from a list.

####### code #######

# import random
# li=[1,2,3,4]

# print(random.choice(li))


# 26. Write a Python program to check whether two lists are circularly identical

######## code ###########

# doubt

# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]

# com = set(list1)&set(list2)
# print(com)




# 27. Write a Python program to find the second smallest number in a list.

###### code #######

# li1=[1, 2, -8, -2, 0, -2]
# li2=[1, 1, 1, 0, 0, 0, 2, -2, -2]

# A=set(li1)
# li1=list(A)
# li1.sort()
# print(li1[1])

# B=set(li2)
# li2=list(B)
# li2.sort()
# print(li2[1])



# 28. Write a Python program to find the second largest number in a list

###### code #######

# li1=[1, 2, -8, -2, 0, -2]

# A=set(li1)
# li1=list(A)
# li1.sort()
# print(li1)
# print(li1[-2])


# 29. Write a Python program to get unique values from a list.

########## code #########

# li1=[1, 2, -8, -2, 0,-2,-8,-8,0]

# A=set(li1)
# li1=list(A)
# print(li1)


# 30. Write a Python program to get the frequency of elements in a list.

###### code #########

# list=[1, 2, -8, -2, 0,-2,-8,-8,0]

# li=[]
# d={}

# for i in list:
#     if i not in li:
#         li.append(i)
#         d.update({i:list.count(i)})


# print(d)



# 31. Write a Python program to count the number of elements in a list within a specified range.

########### code ##########

# min=40
# max=100

# li=[10,20,30,40,40,40,70,80,90]

# for num in li:
#     if(num<min or num>max):
#         li.remove(num)


# print(li)


# 32. Write a Python program to check whether a list contains a sublist

######## code #######

# not solved


# 33. Write a Python program to generate all sublists of a list.

######### code #########

##doubt

# import itertools

# li=list(itertools.combinations(' ',2))
# print(li)




# 34. Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.

#######   code   ########

# li=list()

# for i in range (2,100):
#     count=0
#     for j in range(2,i+1):
#         if(i%j==0 and j<i):
#             count=1
#             break
         
#     if(count==0):
#         li.append(i)     


# print(li)

# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


######## code #########

# li=['p','q']
# n=5     

# new_li=list()

# for i in range(1,6):
#     for char in li:
#         new_li.append(char+str(i))

# print(new_li)


# 36. Write a Python program to get a variable with an identification number or string.

# doubt


# 37. Write a Python program to find common items in two lists.

########## code #########

# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"

# print(set(color1)&set(color2))


# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

######### code ##########

# list=[0,1,2,3,4,5]


# if(len(list)%2==0):
#     lim=len(list)
# else:
#     lim=len(list)-1

# for i in range(0,lim-1,2):
#     list[i], list[i+1] = list[i+1], list[i]
# print(list)    


# 39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

########### code ############

# list=[11, 33, 50]
# s=""

# for num in list:
#     s=s+str(num)


# x=int(s)
# print(x)


# 40. Write a Python program to split a list based on the first character of a word.


######### code #######

# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

# # ['ask', 'be', 'call', 'come', 'do', 'feel', 'find', 'get', 'give', 'go', 'have', 'know', 'leave', 'look', 'make', 'say', 'see', 'seem', 'take', 'tell', 'think', 'use', 'want', 'work']

# # d=dict()
# word_list.sort()
# li=list()

# for i in range(0,len(word_list)-1):

######## doubt


# 41. Write a Python program to create multiple lists

########  code ##########

# d={}

# for i in range(1,11):
#     d[str(i)]=[]

# print(d)


#42. Find missing and additional values in two lists

######### code #########

# list1 = ['a', 'b', 'c', 'd', 'e', 'f']
# list2 = ['d', 'e', 'f', 'g', 'h']

# print("missing value in second list",set(list1).difference(set(list2)))
# print("additional value in second list",set(list2).difference(set(list1)))


# 43. Write a Python program to split a list into different variables.

###### code #####

# color = [
#     ("Black", "#000000", "rgb(0, 0, 0)"),
#     ("Red", "#FF0000", "rgb(255, 0, 0)"),
#     ("Yellow", "#FFFF00", "rgb(255, 255, 0)")
# ]

# for tup in color:
#     print(tup)


# 44. Write a Python program to generate groups of five consecutive numbers in a list.

###### code ########;

# main_list=list()

# for i in range(1,5):
#     li=list()
#     for i in range(1,6):
#         li.append(i)

#     main_list.append(li)

# print(main_list)    


# 45. Write a Python program to convert a pair of values into a sorted unique array.

######## code ########

# li = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]

# n1,n2=zip(*li)

# s1=set(n1)
# s2=set(n2)

# l1=list(s1)
# l2=list(s2)
# l3=l1+l2
# l3.sort
# print(l3)

# ------> doubt tooo long code


# 46. Write a Python program to select the odd items from a list.

##### code ######

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# li=list()
# for num in x:
#     if(num % 2!=0):
#         li.append(num)

# print(li)


# 47. Write a Python program to insert an element before each element of a list.

########  code #########

# color = ['Red', 'Green', 'Black']

# for i in range(0,len(color)*2,2):
#     color.insert(i,'c')

# print(color)


# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.

######## code ########


# colors = [['Red'], ['Green'], ['Black']]

# for li in colors:
#     print(li)

# 49. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]


######### code #########

# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# li=list()

# for i in range(0,len(color_code)):
#     d=dict()
#     d={'color_name':color_name[i],'color_code':color_code[i]}
#     li.append(d)

# print(li)


#50. Write a Python program to sort a list of nested dictionaries.


########## code ###########

# my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]


# my_list.sort(key=lambda e:e['key']['subkey'])
# up_list=list()

# for i in range(0,len(my_list)):
#     r=my_list[i]['key']['subkey']
#     up_list.append(r)


# up_list.sort()

# for i in range(0,len(up_list)):
#     my_list[i]['key']['subkey']=up_list[i]

# print(my_list)
    


# 51. Write a Python program to split a list every Nth element.
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

########## code ########

# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# main_li=list()

# for i in range(0,3):
#     main_li.append(C[i::3])
    

# print(main_li,' ')

# 52. Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

##### code ########

# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]

# print(set(color1).difference(color2))
# print(set(color2).difference(color1))

# 53. Write a Python program to create a list with infinite elements.

####### code ###########

# import itertools

# c=itertools.count()

# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))


# 54. Write a Python program to concatenate elements of a list.

########## code ##########

# color = ['red', 'green', 'orange']
# s=""
# for str in color:
#     s=s+str

# print(s)

# print('-'.join(color))    


# 55. Write a Python program to remove key-value pairs from a list of dictionaries.

######## code ########

# original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]

# for i in range(0,len(original_list)):
#     original_list[i].pop('key1')

# print(original_list)

# 56. Write a Python program to convert a string to a list.

######### code #########
# color = "['Red', 'Green', 'White']"

# # for i in range(0,len(color)):
# #     if(color[i]=='[' or color[i]==']'):
# #         color.replace(color[i],'')


# for alph in color:
#     if(alph=="[" or alph=="]" or alph=="'" or alph=="," ):
#         color.replace(alph,"")
#         print(color)


        ### doubt


# # 57. Write a Python program to check if all items in a given list of strings are equal to a given string

# color1 = ["green", "orange", "black", "white"]
# color2 = ["green", "green", "green", "green"]

# c="green"
# r="true"
# for char in color1:
#     if(c==char):
#         continue
#     else:
#         r="false"
        
# print(r)

# r="true"

# for char in color2:
#     if(c==char):
#         continue
#     else:
#         r="false"

# print(r)


# 58. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

# d1=[1, 3, 5, 7, 9, 10]
# d2=[2, 4, 6, 8]

# d1.remove(d1[len(d1)-1])
# d1.extend(d2)
# print(d1)

# another way

# d1[-1:]=d2
# print(d1)
# print("first -->",d1[-1::])
# print("second -->",d1[::-1])

## doubt

# 59. Write a Python program to check whether the n-th element exists in a given list.

# x = [1, 2, 3, 4, 5, 6]
# print(x[len(x)-1])

# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
####### code ########


# x = [(4, 1), (1, 2), (6, 3),(9,0)]

# a,b=zip(*x)

# min_value=min(b)
# min_index=b.index(min_value)

# print(min_index)

# print(x[min_index])


# 61. Write a Python program to create a list of empty dictionaries.

############ code #############

# n=5
# li=list()

# for i in range(1,n+1):
#     d=dict()
#     li.append(d)
# print(li)


# 62. Write a Python program to print a list of space-separated elements

########### code ##########

# li=[1,2,3,4,5,6]

# print(*li)


# 63. Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

########### code ###########

# list = [1,2,3,4]
# string = "emp"

# for i in range(0,len(list)):
#     s=string+str(list[i])
#     list[i]=s

# print(list)


# 64. Write a Python program to iterate over two lists simultaneously.

####### code ########

# num = [1, 2, 3]
# color = ['red', 'white', 'black']

# for i in range(0,len(color)):
#     print(num[i],color[i])


# 65. Write a Python program to move all zero digits to the end of a given list of numbers.
# Expected output:
# Original list:
# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]



########## code ###########

# Original_list=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# updated_list=list()
# print(Original_list)
# count=0
# for num in Original_list:
#     if(num==0):
#         count+=1
#     else:
#         updated_list.append(num)    

# print(updated_list)     
# r=0
# for i in range(0,count):
#     updated_list.append(r)
     

# print(updated_list)     

# print(Original_list)

# print(sorted(Original_list, key=lambda x:  not x ))

# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]

###### code ####
# lists=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# m=0
# hold=list()
# for li in lists:
#     r=tuple(li)
#     maxi=max(r)
#     if(m<maxi):
#         m=maxi
#         hold=li

# print(hold)       


# 67. Write a Python program to find all the values in a list that are greater than a specified number.

# list1 = [290, 330, 500]
# list2 = [12, 17, 21]  
###### doubt
# print(all(x>=250 for x in list1))


# 68. Write a Python program to extend a list without appending.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

# list1=[10, 20, 30]
# list2=[40, 50, 60]
# #### doubt
# list1[:0]=list2
# print(list1)

# 69. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

# list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# ######## code #######
# li=[]
# for li in list:
#     li.append(tuple(li))    
# ###### doubt
# print(li) 


# 70. Write a Python program to find items starting with a specific character from a list.
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:

########## code #########

# Original_list =['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

# ra=[li for li in Original_list if li[0]=='a']
# rb=[li for li in Original_list if li[0]=='b']
# rc=[li for li in Original_list if li[0]=='c']
# print(ra)
# print(rb)
# print(rc)


# # 71. Write a Python program to check whether all dictionaries in a list are empty or not.
# # Sample list : [{},{},{}]
# # Return value : True
# # Sample list : [{1,2},{},{}]
# # Return value : False

# Sample_list = [{},{1},{}]
## doubt
# print(all(not d for d in Sample_list))


#72 Write a Python program to flatten a given nested list structure.
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


# Original_list=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

# li=[]

# for li1 in Original_list:
#     if(type(li1)==list):
#         li.extend(li1)
#     else:
#         li.append(li1)

# print(li)    


# 73. Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]


# Original_list=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# print(set(Original_list))

# 74. Write a Python program to pack consecutive duplicates of a given list of elements into sublists.
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]


Original_list=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# 75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.
# Original list:
# [1, 1, 2, 3, 4, 4.3, 5, 1]
# List reflecting the run-length encoding from the said list:
# [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# Original String:
# automatically
# List reflecting the run-length encoding from the said string:
# [[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]

# from itertools import groupby
# Original_list=[1, 1, 2, 3, 4, 4.3, 5, 1]

# re=[[len(list(group)), key] for key, group in groupby(Original_list)]
# print(re)

# import itertools

# list=['black','cat','cammando']

# count=1
# for i in itertools.cycle(list):
#     if count >=7:
#         break
#     else:
#         print(i)
#         count+=1


# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

import itertools
Original_list=[1, 1, 2, 3, 4, 4, 5, 1]

x=list()

# for key,group in itertools.groupby(Original_list,key=lambda x:x):
#     r=len(list(group))
#     if(r>1):
#         li=list()
#         li.append(r)
#         li.append(key)
#         x.append(li)
#     else:
#         x.append(key)    

# print(x)


######## by list comprehsion #######

# def val(key,group):
#         r=len(list(group))
#         if(r>1):
#             li=list()
#             li.append(r)
#             li.append(key)
#             return li   
#         else:
#               return key

# updated_list=[val(key,group)  for key,group in itertools.groupby(Original_list,key=lambda x:x)]


# print(updated_list)

# s="abracadabra "

# li=list(s)

# li[5]='k'

# s=str(li)
# print(li)
# str1=""
# s=str1.join(li)
# print(s)


s="missiccippi"
li=[]
for i in s:
    if i not in li:
        li.append(i)

print(li)
d={}
for i in range(len(li)):
    d.update({i:li[i]})

print(d)