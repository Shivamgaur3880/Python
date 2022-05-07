with open('z_this.txt') as f:
    content=f.read()

with open('z_copied.txt','w') as f:
    f.write(content)