#Snakes and laders
from random import randint
p=dict()    # we use a dictionary to store the players names and their positions in key-value pairs. This method also helps in easy allocation of exactly one chance to each player in one round
# the initial and final positions of snakes and ladders are stored as a key value pairs in a dictionary
# for example "2:38" a ladder starts at 2(initial) and takes you to 38(final)
perks={2:38,7:14,8:31,15:26,21:42,28:84,36:44,51:67,71:91,78:98,87:94,99:80,95:75,74:53,64:60,62:19,49:11,46:25,16:6}
win=None


# a function to update the positions of the players and also to check the snakes and ladders cases and 1,5,6 dice conditions
def update(pla,t):
    if p[pla]+t>100:
        return
    p[pla]+=t
    p[pla]=perks.get(p[pla],p[pla])
    print(p)
    if t in {1,5,6}:
        print(pla,'roll the Dice again.')
        input()
        t=randint(1,6)
        print('You got',t)
        update(pla,t)
        
# Driver code
for i in range(1,int(input('Number of players:'))+1):
    p[input("Player "+str(i)+" name:")]=0                                                  # we intialize every players postion to 0
print("\n\nEnter the space button to roll the dice\n---------Let's start the game----------")
while 100 not in p.values():                                                               # loop brakes when a player reaches 100
    for i in p:
        print(i,'roll the Dice.')
        input()
        t=randint(1,6)                                                                     # randit to generate a number from 1 to 6
        print('You got',t)
        update(i,t)
        if p[i]==100:
            win=i
            break
print('Congrats',win,'!!!!')
