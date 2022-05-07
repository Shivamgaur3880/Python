import os

oldname= 'z_sample3.txt'
newname='z_renamed_by_python.txt'
with open(oldname) as f:
    content=f.read()


with open(newname,'w') as f:
    f.write(content)


os.remove(oldname)