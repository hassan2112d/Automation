# read method read the file till the end from where it is leave in script and readline read only onne line
#you should have to use close() function to close the operating of files or you can use with to avoid it.

# a = open("intro.txt")


# print(a.readline())



# print(a.read())

#close(a)

with open("intro.txt") as a:
    print (a.read())