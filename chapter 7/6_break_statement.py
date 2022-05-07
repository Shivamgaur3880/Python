for i in range(10):
    
    if i==5:
        break
    print(i)
else:    # not run else because for loop terminate unexpected
    print("This is inside else of 'For'")