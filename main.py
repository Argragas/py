from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 12, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]


player = Person(460, 65, 60, 34,  magic)
enemy = Person(1200, 65, 45, 25,  magic)

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
        magicdmg = player.generate_spell_damage(magic_choice)
        cost = player.get_spellcost(magic_choice)
        
        if cost > player.get_mp():
            print(bcolors.FAIL + "Not enough MP" + bcolors.ENDC)
            continue
        else:
            player.reduce_mp(cost)
            enemy.take_damage(magicdmg)
            print(bcolors.OKBLUE + player.get_spellname(magic_choice)) + " deals" + str(magicdmg) + " points of damage" + bcolors.ENDC
            
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
