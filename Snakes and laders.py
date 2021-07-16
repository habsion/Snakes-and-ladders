#Snakes and laders
from random import randint
p=dict()
perks={2:38,7:14,8:31,15:26,21:42,28:84,36:44,51:67,71:91,78:98,87:94,99:80,95:75,74:53,64:60,62:19,49:11,46:25,16:6}
win=None
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
for i in range(1,int(input('Number of players:'))+1):
    p[input("Player "+str(i)+" name:")]=0
print("\n\nEnter the space button to roll the dice\n---------Let's start the game----------")
while 100 not in p.values():
    for i in p:
        print(i,'roll the Dice.')
        input()
        t=randint(1,6)
        print('You got',t)
        update(i,t)
        if p[i]==100:
            win=i
            break
print('Congrats',win,'!!!!')