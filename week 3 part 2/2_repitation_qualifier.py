#Practise question

# import re
# def long_words(text):
#   pattern = r"\w{7,}"
#   result = re.findall(pattern, text)
#   return result

# print(long_words("I like to drink coffee in the morning.")) # ['morning']
# print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
# print(long_words("I never drink tea late at night.")) # []



import re

print(re.search(r"[a-zA-Z]{5}","a ghost"))

print(re.search(r"s\w{,20}","i really like a strawberries"))

print(re.findall(r"\w{5,}","I really like strawberries"))

