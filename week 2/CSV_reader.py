import csv

f = open("second.html")

hello = csv.reader(f)

for row in hello:
    name,age,surname= row
    print("Name : {} , Age : {} , Surname : {} ".format(name,age,surname))

f.close()