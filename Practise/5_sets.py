s1={1,1,1,1,1,2,2,2,2,3,4,5,6,6,6,6,7,7,7,"harsh"}
print(s1)

s1.add("rohan")
print(s1)
s1.add("rohan1")    # last me add kardega kahi bhi
print(s1)
s1.add(999)
print(s1)


s1.update("rohan":"33")


# s1.remove(99)
s1.discard(99)    #doesn't give error
print(s1)

s1.pop()
print(s1)


s1.clear()
print(s1)

# del s1[2]    #doesn't support
# print(s1)