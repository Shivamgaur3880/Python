from os import times


story= '''once upon a time there is old world 
          all people fight with each other and then 
            god comes teaches the lesson of karma '''

print(len(story))   #length of string
print(story.endswith("karma"))     # tells string ends with
print(story.count("old"))         # count word/character
print(story.capitalize())      #capital first word of string
print(story.find("time"))     #find word return index of 1st occurance,give -1 if not find
print(story.replace("god","godfather"))  #replace with new in entire string