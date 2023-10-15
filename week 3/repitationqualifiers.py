import re

#dot complete the one word and * complete the whole word
print(re.search(r"Py.*n","Python"))

print(re.search(r"Py[a-z]*n","Python"))

print(re.search(r"Py[A-Z]*n","Python"))

#+ sign 

print(re.search(r"o+l","lool"))

#A is repeating
import re
def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

#? question mark is a optional thing like if it is present it takes it or if it doesnt present it not matches it.

print(re.search(r"h?ello","hello"))

print(re.search(r"h?ello","ello"))