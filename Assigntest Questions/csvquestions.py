
# Question No 1

# import os
# import csv

# # Create a file with data in it
# def create_file(filename):
#   with open(filename, "w") as file:
#     file.write("name,color,type\n")
#     file.write("carnation,pink,annual\n")
#     file.write("daffodil,yellow,perennial\n")
#     file.write("iris,blue,perennial\n")
#     file.write("poinsettia,red,perennial\n")
#     file.write("sunflower,yellow,annual\n")


# # Read the file contents and format the information about each row
# def contents_of_file(filename):
#   return_string = ""

#   # Call the function to create the file 
#   create_file(filename)

#   # Open the file
#   with open(filename,"r") as h:

#     # Read the rows of the file into a dictionary
#     f = csv.DictReader(h)
#     # Process each item of the dictionary
#     for row in f:
#       return_string += "a {} {} is {}\n".format(row["name"], row["color"], row["type"])
#   return return_string


# #Call the function
# print(contents_of_file("flowers.csv"))


# Question no 2

# import os
# import csv

# # Create a file with data in it
# def create_file(filename):
#   with open(filename, "w") as file:
#     file.write("name,color,type\n")
#     file.write("carnation,pink,annual\n")
#     file.write("daffodil,yellow,perennial\n")
#     file.write("iris,blue,perennial\n")
#     file.write("poinsettia,red,perennial\n")
#     file.write("sunflower,yellow,annual\n")

# # Read the file contents and format the information about each row
# def contents_of_file(filename):
#   return_string = ""

#   # Call the function to create the file 
#   create_file(filename)

#   # Open the file
#   with open(filename, "r") as file:
#     # Create a CSV reader
#     csv_reader = csv.reader(file)
    
#     # Skip the header row
#     next(csv_reader)
    
#     # Process each row
#     for row in csv_reader:
#       name, color, flower_type = row
      
#       # Format the return string for data rows only
#       return_string += "a {} {} is {}\n".format(name, color, flower_type)
      
#   return return_string

# # Call the function
# print(contents_of_file("flowers.csv"))
