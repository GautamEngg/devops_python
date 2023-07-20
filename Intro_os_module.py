# os module 
# use to python to execute some operating system command

import os 
print(dir(os))
print(help(os))

# Run linux command using os module
os.system("ls -l")
os.system("ls -lrth")
os.system("pwd")
os.system("cp filename.ext path/of/destination")

# save output of command in a variable 
a = os.system("ls -l")
print("value of a =", a)
#os.system command does not store the output of the command 
#it stores the exit code of the command
#subprocess module is used to store the output, logs, error and whole result of the command 

os.system("pwd")            #print working directory
os.getcwd()                 #print current working directory
# os.chdir("/tmp")            #change working directory
# os.chdir("/home/username")  #change working directory back to home

os.listdir()
os.listdir("path_of_directory")


for i in os.listdir():
    print(i)

# Create a file using OS module
os.mknod("test_file_creation_osmodule")
os.listdir()

#create new directory
os.mkdir("newdir")
#create new directory recursively
os.mkdir("newdir/dir1")

#to get environment variables
os.environ

#to get specipic environment variable
os.environ.get("PATH")
os.environ.get("PWD")
os.getuid()

#to remove/delete directory
os.rmdir("newdir2")
#to remove/delete directory recursively
os.removedirs("newdir/dir1")






