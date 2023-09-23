import csv
#//Writing and generating csv file
hii = [["Hassan","hiii"],["hasnain","hello"]]

with open("hello.csv","w") as hello:
    writer =  csv.writer(hello)
    writer.writerows(hii)

#//Readng this file

# f = open("hello.csv")
# h = csv.reader(f)

# for row in h:
#     name,msg = row
#     print("Name : {} , Msg : {}".format(name,msg))

# f.close()