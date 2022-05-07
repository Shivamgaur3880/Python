
def game():
    return 619


score=game()

with open('z_hiscore.txt','r') as f:
    prev_score=f.read()
if prev_score=='':
    with open('z_hiscore.txt','w') as f:
        f.write(str(score))
elif int(prev_score)<score:
    with open('z_hiscore.txt','w') as f:
        f.write(str(score))
