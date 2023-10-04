
#Normal method 

# a = "July 19 my name is hasssan . my ubit attendence id is [57]"

# b = a.index("[")

# print(a[b+1:b+3])

#Now through regular expressions moduele

import re

a = "July 19 my name is hasssan . my ubit attendence id is [56]"
b = r"\[(\d+)\]" # This is a syntax for digit 
d = re.search(b,a) # This is a syntax for search

print(d[1])
