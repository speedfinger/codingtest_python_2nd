from collections import defaultdict

str_dict = defaultdict(int)
str_dict['abc']=1

print(str_dict)
print(str_dict["abc"])
print(str_dict["abca"])