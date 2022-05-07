with open('z_poem.txt','r') as f:
    a=f.read()

    b=a.find('sky')       # upper and lower case matters
    if b==-1:
        print(f"sky is not present")
    else:
        print(f"sky is present at {b}")


if 'z_twinkle' in a:
    print('yes')
else:
    print('no')