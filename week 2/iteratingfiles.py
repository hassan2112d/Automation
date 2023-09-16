with open("intro.txt") as b:
    for c in b:
        print(c.upper().strip())


# if i will only put uppercase so it will take  a character as a line so overcome this python provides strip method to 
# delete the line .

#Now how to readlines method  it and check it is showing me the lines by character or not.

files = open("intro.txt")

hello = files.readlines()

hello.sort()
print(hello)

files.close()