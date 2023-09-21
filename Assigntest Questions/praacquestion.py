#Q1 The create_python_script function creates a new python script in the current working directory, 
#adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file.
#Fill in the gaps to create a script called "program.py".

# import os
# def create_python_script(filename):
#     comments = "# Start of a new Python program"
#     with open(filename, 'w') as file:
#         file.write(comments)  # Write the comments to the file
#     filesize = os.path.getsize(filename)  # Get the size of the new file
#     return filesize

# print(create_python_script("program.py"))


#Q2 The file_date function creates a new file in the current working directory, 
#checks the date that the file was modified, and returns just the date portion of the timestamp in the
# format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the
# date that it was modified. 

# import os
# import datetime

# def file_date(filename):
#     # Create the file in the current directory
#     with open(filename, 'w') as file:
#         pass  # An empty 'with' block just creates the file

#     # Get the modification timestamp of the file
#     timestamp = os.path.getmtime(filename)

#     # Convert the timestamp into a readable format as a datetime object
#     date_modified = datetime.datetime.fromtimestamp(timestamp)

#     # Format the date as "yyyy-mm-dd" and return it as a string
#     return date_modified.strftime("%Y-%m-%d")

# # Example usage:
# print(file_date("newfile.txt"))


#Q3 The new_directory function creates a new directory inside the current working directory, then creates 
#a new empty file inside the new directory,and returns the list of files in that directory. 
#Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".    


# import os

# def new_directory(directory, filename):
#     # Before creating a new directory, check to see if it already exists
#     if not os.path.exists(directory):
#         os.mkdir(directory)  # Create the new directory

#     # Create the new file inside of the new directory
#     os.chdir(directory)  # Change the current working directory to the new directory
#     with open(filename, 'w') as file:
#         pass  # An empty 'with' block just creates the file

#     # Return the list of files in the new directory
#     files_in_directory = os.listdir()
#     return files_in_directory

# print(new_directory("PythonPrograms", "script.py"))
