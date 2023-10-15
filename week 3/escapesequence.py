import re

print(re.search(r".com","welcome"))

#if i put \  backslash it will take dot as a string

print(re.search(r"\.com","mydomain.com"))

#\w use for to match special character like numbers , letters, alphanumeric character but space is not in it

print(re.search(r"\w*","This is a toys"))

print(re.search(r"\w*","This_is_a_toys"))

#\b is used for word boundries means the first and last one

#\s is used for spaces 

