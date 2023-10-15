import re


print(re.search(r"A.*a","Argentina"))

#it will end on a
print(re.search(r"A.*a","Azarbaijan"))

#to end with given letter we should use dollar sign

print(re.search(r"A.*a$","Azarbaijan"))
