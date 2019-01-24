from classes.game import Person, bcolors
from classes.magic import Spell

fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 12, 124, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 12, 120, "Black")

cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")


player = Person(460, 65, 60, 34,  [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25,  [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTAKS !" + bcolors.ENDC)


while running:
    print("===================")
    player.choose_action()
    choice = input("Choose action :")
    index = int(choice) - 1
    print("You chose", choice)
     
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic :")) -1
        
        spell = player.magic[magic_choice]
        magicdmg = spell.generate_damage()
       
        if spell.cost > player.get_mp():
            print(bcolors.FAIL + "Not enough MP" + bcolors.ENDC)
            continue
        else:
            player.reduce_mp(spell.cost)
            
            if spell.type == "White":
                player.heal(magicdmg)
                print(bcolors.OKGREEN + spell.name, "heals for", dmg, bcolors.ENDC)
            else:
               enemy.take_damage(magicdmg)
               print(bcolors.OKBLUE + spell.name, " deals" + str(magicdmg), " points of damage" + bcolors.ENDC)
            
    enemy_choice = 1
    enemydmg = enemy.generate_damage()
    player.take_damage(enemydmg)
    print("Enemy attacked for", enemydmg, "points of damage.")

    print("===================")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)
    print("Player HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    print("Player MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC)
    
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy defeated you!" + bcolors.ENDC)
        running = False
