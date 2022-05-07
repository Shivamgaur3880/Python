word_list=["wonder","donkey","drama","fruits","flower"]

with open("z_donkey.txt") as f:    # 1st Step
    content=f.read()                      

for i in word_list:
    content = content.replace(i,"*")               #  2nd Step
    with open("z_donkey.txt","w") as f:           #  3rd Step
        f.write(content)