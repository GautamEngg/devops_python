import os

#os.path
#os.walk

#.....1. os.path..........
#return all attributes of os.path
a = dir(os.path)
print(a); 

#check path exists or not 
os.path.exists("/etc/hosts")
os.path.exists("__name__")

#Check size of the file in bytes
os.path.getsize("os_module_into.py")
#check basename of a path (in this case base name of /etc/hosts is hosts)
os.path.basename("/etc/hosts")
#Join/concatinate 2 paths ( /home + os_module = /home/os_module ) 
os.path.join("/home", "os_module")


#.....2. os.walk...........
# os.walk is used to print the directory tree and all files in directory tree

os.walk("/etc/hosts")

#print all files and directories inside the home directory
print(list(os.walk("/home")))




