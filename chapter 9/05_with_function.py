with open('z_sample.txt','r') as a:
    data=a.read()
    print(data)


with open('z_sample.txt','a') as a:
    a.write("\tgood")
    print(data)
    