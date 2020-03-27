import os

allfiles = os.walk(r"c:\classroom\feb28\demo")

for (dirname, folders, files) in allfiles:
    for f in files:
        if f.endswith('.py'):
           print(dirname + "\\" + f)
