with open("z_donkey.txt",'r') as f:    # 1st Step
    a=f.read()                      

convert = a.replace('donkey','#')               #  2nd Step


with open("z_donkey.txt",'w') as f:           #  3rd Step
    f.write(convert)
