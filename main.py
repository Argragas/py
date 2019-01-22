import random


class Enemy:
    hp = 200
    
    # run a l'instanciation
    def __init__(self, enemyatk_min, enemyatk_max):
        self.enemyatk_min = enemyatk_min
        self.enemyatk_max = enemyatk_max
    
    def get_attak(self):
        print("attaque min :",self.enemyatk_min)
    
    def get_hp(self):
        print(self.hp,"point(s) de vie")
        
        
en1= Enemy(40, 40)
en1.get_attak()
en1.get_hp()

en2 = Enemy(60, 80)
en2.get_attak()

'''
playerhp = 260
while playerhp > 0:
    damage = random.randrange(enemyatk_min, enemyatk_max)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30


    print("Dommage :", damage, "points de vie restant :", playerhp)

    if playerhp > 30:
        continue

    print("point de vie bas")
    break
'''

