import re

# For uppercase and lower case
print(re.search(r"[Pp]ython","python"))

print(re.search(r"[a-z]ello","hello"))

# check the space which is different from small letters
print(re.search(r"[^a-z]","hello my name is hassan."))

# check the space which is different from small and capital  letters
print(re.search(r"[^a-zA-Z]","hello my name is hassan."))

#check the dog or cat

print(re.search(r"cat|dog","the cat is cute"))

print(re.search(r"cat|dog","the dog is cute"))

#if both it will take out the first one

print(re.search(r"cat|dog","the dog is cute and cat as well"))

#if you want to find all then use findall function

print(re.findall(r"cat|dog","the cat and dogs are cute"))