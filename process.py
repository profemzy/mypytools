import subprocess
pl = subprocess.Popen(['ps', '-u', '0'], stdout=subprocess.PIPE).communicate()[0]

# list out all the running processes in the system as a child process
print(pl.decode('utf-8'))