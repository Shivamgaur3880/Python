newdict={"fast":"in a quick manner",
"harry":"a coder",
"marks":[1,2,3],
"anotherdict":{"god":"shiv"},
1:2
}
print(newdict.keys())  # also.... print(list(newdict.keys()))
print(newdict.values())   # also..... print(list(newdict.values()))
print(newdict.items())   # print keys and values
updatedict={"lovish":"friend",
"ratan":"friend",
"janak":"friend",
"hridya":"friend"}
newdict.update(updatedict)
# print(newdict)
print(newdict.get("ratan"))  # return none if not found
print(newdict["ratan"])        # throws error if not found