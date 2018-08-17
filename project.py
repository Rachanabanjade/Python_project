#Write a script to search any file extension in your laptop. (1 Student)
#For example: if I give query as &quot;png&quot;, your program should list all png image files
#that are in your system.

import os
ext = input("Which extension do you want to search: ")
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
         if file.endswith("."+ext):
             print(os.path.join(root, file))