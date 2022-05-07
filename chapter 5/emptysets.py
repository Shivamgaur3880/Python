# a={}        # create dictionary not set
a=set()
print(type(a))
#   operation on sets

a.add(4)
a.add(4)   #add only once
a.add(5)
a.add(5)
a.add(6)
a.add(6)   
a.add(7)
a.add(8)
print(a)
# a.add([999,111])              can't add list
# a.add({"janak":"friend"})   can't add dictionary
a.add((9,8,7))    #  we can add tuples ....they are unchangable
print(a)
print(len(a))   #length
a.remove(4)     # remove
print(a)
a.pop()       # remove random element
print(a)
print(a.union({8,11}))              #print both sets
print(a.intersection({8,11}))          # print common element