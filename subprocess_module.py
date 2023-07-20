import subprocess

# using os module we cannot store the output of the command, we can only store the exit code. 
# Subprocess module is used to store the output of the command.

#to create a new process using the subprocess we can use a library fucntion called subprocess.Popen

cmd = ["ls", "-lrth"]   #mention command as list if shell=false
# cmd = "ls -lrth"        #mention command as string if shell=true


# try to avoid shell=True
# if a python program is running with shell=true it fork a new shell
# python --> shell=True --> fork --> shell(syntex or symentics) (it may lead to security leaks)


var = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

rt = var.wait()
out,err=var.communicate()
print(out)
print(err)


