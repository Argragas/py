import random

playerhp = 260
enemyatk_min = 60
enemyatk_max = 80


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


