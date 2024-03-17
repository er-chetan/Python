####################################
###### to list all the methods of string
# print(dir(''))

###### to find length of a string
# print(len('Hello'))

#######---- STRING METHOD------#######

a="hellO World"
########----LOWER ALPHABETS----######
# print(a.lower())
# print(a.casefold())

########----UPPER ALPHABETS----######
# print(a.upper())

b="Hello World"

########----swap upper to lower and lower to upper ALPHABETS----######

# print(b.swapcase())

####---every word first letter is captial----####

# c='hello world'
# print(c.title()) 

####-----center the string from left right---####

# print(a.center(60))
# print(a.center(60,'-'))


#####----only first letter of string is captalize-----####
# d="hello world"
# print(d.capitalize())

#####---- join the alphabet after every letter------####
# print('-'.join(a))

#space from right of the string
# print(a.ljust(60,'-'))

#space from left of the string
# print(a.rjust(60,'-'))


#### to count no of any repetitive characters 
# print(a)
# print(a.count('o'))
# print(a.count('l'))


# print(a.index('l'))
# print(a.rindex('l'))
# print(a.index('l',3))
# print(a.index('l',4,8))


# print(a.find('l'))
# print(a.rfind('l'))
# print(a.find('l',3))
# print(a.find('l',4,8))

# print(a.replace('l','z'))


b = "          helloo        world        "
# print(b.strip())
# print(b.lstrip())
# print(b.rstrip())
# print((b.replace('        ','')).strip())

# b = "https://www.techgeecs.com/"
# print(b.lstrip('https://www'))
# print(b.rstrip('.com/'))
# print(b.removeprefix('https://www.'))
# print(b.removesuffix('.com/'))

# b = "India is my country"
# print(b.split())
# print(len(b.split()))


# print(b.split('i'))
# print(b.rsplit('i'))

# c= "India is my country.\nIlove my country.\n"
# print(c.splitlines())


# print('1234'.zfill(8))

# print('hello\twor\tld'.expandtabs(24))

##########

# print('Hello'.endswith('llo'))
# print('Hello'.startswith('He'))

# print(a)
# print(a.isalnum())
# print(a.isalpha())
# print(a.isascii())


d = '12324'
e ='12312423.34234'

# print(d.isdecimal())
# print(e.isdecimal())
# print(e.isnumeric())
# print(e.isdigit())

g= 'Hello World'
# print(g.isidentifier())
# print(g.islower())
# print(g.isupper())
# print(g.istitle())
print(g.isprintable())

# print('\t\n '.isspace())



######'format'

a = 2
b=3
c=4
d=5
# print("value of a =",a,"\t value of b =",b,"\t value of c =",c, "\t value of d =",d)

# print("\n value of a = {} \n value of b = {} \n value of c  ={} \n value of d ={}".format(a,c,b,d))
# print("\n value of a = {0} \n value of b = {1} \n value of c  ={2} \n value of d ={3}".format(a,b,c,d))

# print("\n value of a = {p} \n value of b = {q} \n value of c  ={r} \n value of d ={s}".format(p=a,q=b,r=c,s=d))


# print(f"\n value of a = {a} \n value of b = {b} \n value of c  ={c} \n value of d ={d}")
