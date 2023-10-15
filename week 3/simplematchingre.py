import re

print(re.search(r"pong","pongfinity"))

print(re.search(r"ping","pingfinix"))

print(re.search(r"p.ng","pongfinity"))

# Casesensitive

print(re.search(r"ss","hasSan",re.IGNORECASE))