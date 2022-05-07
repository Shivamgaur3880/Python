text=input("enter your text\n")

if("make a lot of money" in text):
    # print("spam")
    spam=True                 # another way

elif("buy now" in text):
    # print("spam")
    spam=True

elif("subscribe this" in text):
    # print("spam")
    spam=True

elif("click this" in text):
    # print("spam")
    spam=True

else:
    spam=False
############################################
if(spam):
    print("spam")

else:
    print("safe")