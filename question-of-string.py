############# calculate the length of the string

########## code  ##########
# count=0
# str ="w3resource"
# for char in str:
#     count+=1
# print(count)  
# print(len(str)) 





#######  Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

########## code  ##########
# str="google.com"
# a=[]
# b={}

# for i in str:
#     if i not in a:
#         a.append(i)
#         b.update({i:str.count(i)})

# print(b)




# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

########## code  ##########

# str="w3resource"

# if(len(str)<2):
#     print("less")
# else:
#     print(str[0:2]+str[-2:])    





# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t

########## code  ##########

# str="restart"
# fc=str[0]
# str=str.replace(fc,'$')
# str=fc+str[1:]
# print(str)    





# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

# a="abc"
# b="xyz"
# new=a[0:]+' '+b[-len(b)-1:]
# print(new)





# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

########### code ##########

# str="abcing"

# if(len(str)<3):
#     print("less")
# else:
#     if(str[-3:]=="ing"):
#         str=str+"ly"
#     else:
#         str=str+"ing"
    

# print(str)






# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

########### code ##########
# str='The lyrics is not that poor!'

# if('not' in str and 'poor' in str):
#     str=str[0:str.index("not")]
#     str=str+"good"
#     print(str)
# else:
#     print(str)    