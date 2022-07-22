import re

text = "My number is 123456789 and I hope you have a nice day, hope every thing well"

patt = "hope"

match = re.search(patt, text)

print(match.group())
print(match.span())
print(match.start())
print(match.end())

text_1 = "hello, heabo, hecdo, he56o, heaao, heoooo, heeeeeeeeeee, he568o, he52335412, he+!o, a b c"

print(re.findall(r"he[abcl][a-d]o", text_1))
print(re.findall(r"he..o", text_1))
print(re.findall(r"he*", text_1))
print(re.findall(r"he+e", text_1))
print(re.findall(r"he\d{2}o", text_1))
print(re.findall(r"he\d{1,3}o", text_1))
print(re.findall(r"he\d{1,}o", text_1))

print("--------------------------------------")
# d number ---------- D not number
print(re.findall(r"he\d\do", text_1))
print(re.findall(r"he\D\Do", text_1))
# w characters or number
print(re.findall(r"he\w\wo", text_1))
# + ? ! or more
print(re.findall(r"he\W\Wo", text_1))

print("---------------------------------------")
# \s space key
print(re.findall(r"a\sb\sc", text_1))
# any not space
print(re.findall(r"\S\S\S\S\S", text_1))

text_2 = "my phone number is 456-458-4528, and 008-4121535"
print(re.findall(r"\d\d\d-\d\d\d-\d\d\d\d", text_2))
print(re.findall(r"00\d-\d*", text_2))

text_3 = "my phone number is 0008-4121535"
print(re.findall(r"0+\d-\d*", text_3))

text_4 = "Here is my address 2000-building3-street, send me letter when you get time, remember is 2000 not 2001"
print(re.findall(r"\d+-\w*-street", text_4))
print(re.findall(r"\b2000", text_4))
print(re.findall(r"\b2000\b", text_4))

text_5 = "Are you a dog person or cat person"
print(re.findall(r"dog|cat", text_5))
