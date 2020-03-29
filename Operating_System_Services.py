import os
#  1. Write a Python program to get the name of the operating system (Platform independent),
#  information of current operating system, current working directory, print files and directories
#  in the current directory and raises error in the case of invalid or inaccessible file names and paths.
print(os.name)
print(os.getcwd())
print(os.listdir())

# 2. Write a Python program to list only directories, files and all directories, files in a specified path.
print(os.listdir("E:\\"))

# 3. Write a Python program to scan a specified directory and identify the sub directories and files.
# Click me to see the sample solution

for i in os.scandir("E:\\"):
    print(i, end="")
#
# 4. Write a Python program to check for access to a specified path. Test the existence, readability, writability
# and executability of the specified path. Go to the editor
# Click me to see the sample solution
print(os.access("E:\\", 2))

# 5. Write a Python program to get the size, permissions, owner, device, created, last modified and last accessed date
# time of a specified path. Go to the editor
# Click me to see the sample solution
#
# 6. Write a Python program to create a symbolic link and read it to decide the original file pointed by the link.
#
# 7. Write a Python program to create a file and write some text and rename the file name. Go to the editor
# Click me to see the sample solution
#
# 8. Write a Python program to find the parent's process id, real user ID of the current process and change real
# user ID. Go to the editor
# Click me to see the sample solution
#
# 9. Write a Python program to retrieve the current working directory and change the dir (moving up one).
#
# 10. Write a python program to access environment variables and value of the environment variable. Go to the editor
# Click me to see the sample solution
#
# 11. Write a Python program to iterate over a root level path and print all its sub-directories and files
# , also loop over specified dirs and files. Go to the editor
#

# 12. Write a Python program to test whether a given path exists or not. If the path exist find the filename
# and directory portion of the said path. Go to the editor
# Click me to see the sample solution

os.path.exists()

# 13. Write a Python program to join one or more path components together and split a given path in directory and
# file. Go to the editor
# Click me to see the sample solution
#
# 14. Write a Python program to alter the owner and the group id of a specified file. Go to the editor
# Click me to see the sample solution
#
# 15. Write a Python program to get information about the file pertaining to the file mode. Print the information
# - ID of device containing file, inode number, protection, number of hard links, user ID of owner, group ID of
# owner, total size (in bytes), time of last access, time of last modification and time of last status change.
