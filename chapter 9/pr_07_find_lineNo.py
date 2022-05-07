
content=True
i=1
with open("z_log.txt") as f:
    
    while content:
        content=f.readline()
        if 'python' in content.lower():
            print(f"yes python is present in line {i}")
        else:
            pass
        i+=1