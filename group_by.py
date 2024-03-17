
import itertools

robots = [
    {"name": "blaster", "faction": "autobot"},
    {"name": "galvatron", "faction": "decepticon"},
    {"name": "jazz", "faction": "autobot"},
    {"name": "metroplex", "faction": "autobot"},
    {"name": "megatron", "faction": "decepticon"},
    {"name": "starcream", "faction": "decepticon"},
]

# c=sorted(robots,key=lambda x: x['faction'])
# print(c)

# for key, group in itertools.groupby(c,key=lambda x: x['faction']):
#     print(key,":",)
    # print(list(group))



list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat','wombat', 'mongoose', 'malloo', 'camel']

c= sorted(list_things, key = lambda x: x[0])
# print(c) ;

dic = {}
for key,group in itertools.groupby(c,key=lambda x:x[0]):
    dic[key] = list(group)

print(dic)    
