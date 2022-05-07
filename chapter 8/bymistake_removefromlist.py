word_list=['hello','good','clear','god','yagya','madhuban']

word=input("enter word to remove\t")

def remove():
    if word in word_list:
        word_list.remove(word)
        print(word_list)
    else:
        print("enter word present in list")

remove()
