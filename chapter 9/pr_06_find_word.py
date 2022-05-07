with open('z_log.txt') as f:
    content= f.read()

if 'python' in content.lower():
    print("yes python is present")
else:
    print("not present")