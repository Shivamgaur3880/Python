temp= int(input("enter tempreture in celcius"))

def convert(temp):
    return (temp*1.8)+32

tempreture = convert(temp)

print(f"faranheight tempreture is {tempreture}")