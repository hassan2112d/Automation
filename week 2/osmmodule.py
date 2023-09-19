import os

#os.rename("first.html","second.html")

#os.remove("hello.txt")

print(os.path.exists("intro.txt"))

#it give the size of the file

print(os.path.getsize("second.html"))

#it gives the unixtimestamp from 1 janvury 1970 
#print(os.path.getmtime("second.html"))

#if i want to change it into human understandable form of date time then

import datetime
timestamp = os.path.getmtime("second.html")

print(datetime.datetime.fromtimestamp(timestamp))

#Give you the Path of the file
print(os.path.abspath("second.html"))