import csv

#Dictonary writer arranged the big data in formated row and coloumn and also have a function to give accourding to coloumn

# a = [{"name":"Hassan","age":"19","subject":"CS"},
#      {"name":"razabbas","age":"19","subject":"Media"},{"name":"Muslim","age":"19","subject":"CS"},
#      {"name":"Shayan","age":"20","subject":"SE"}]

# keys = ["name","age","subject"]


# with open("bye.csv","w") as h:
#     b = csv.DictWriter(h, fieldnames=keys)
#     b.writeheader()
#     b.writerows(a)

#Dictonary reader read data accourding to row and coloumn because of big data

with open("bye.csv","r") as a:
    b = csv.DictReader(a)
    for row in b :
        print ("Name : {} , Age : {} , Subject :{}" .format(row["name"],row["age"],row["subject"]))