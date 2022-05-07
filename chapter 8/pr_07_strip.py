string= "               hello how are you               "

def remove(strings,word):
    a=string.replace(word,"")
    return a.strip()

b=remove(string,"are")
print(b)
