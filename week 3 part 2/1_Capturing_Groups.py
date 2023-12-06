import re


# Revision Practise
# pattern = "^[A-Z][a-z]+[.?!]$"

# text = "Hassan!"

# print(re.search(pattern,text))

result = re.search(r"^(\w*), (\w*)$","Helloworld, astra")

print(result)

print(result.groups())

print(result[0])

print(result[1])
print(result[2])

print("{}{}".format(result[2],result[1]))