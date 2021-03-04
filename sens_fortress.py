from sys import exit
from random import randint

player_health = 100

winged_spear = False
lightning_spear = False
zweihander = False
no_estus = False
tarkus = False

snake = [100, 20, 25, "Serpent Soldier strikes"]
s_k = [160, 20, 50, "Silver Knight strikes"]
mimic = [100, 45, 50, "Mimic swipes"]
patches = [100, 30, 35, "Dude"]
demon = [200, 30, 35, "Titanite Demon swings"]
be_k = [200, 30, 50, "Berenike Knight bashes"]
mage = [120, 30, 40, "Serpent Mage casts a lightning spell"]
boss = [650, 30, 40, "Iron Golem swings its cleaver"]

def enemy(enemy_health, range_1, range_2, enemy_name):
    global player_health
    global no_estus
    global winged_spear
    global lightning_spear
    global zweihander
    global tarkus

    for combat_turns in range(9999):

        if winged_spear == True:
            damage_dealt = randint(1,1)
            damage_taken = randint(range_1, range_2)
        elif zweihander == True:
            damage_dealt = randint(50, 90)
            damage_taken = randint(range_1, range_2)
        elif lightning_spear == True:
            damage_dealt = randint(60,60)
            damage_taken = randint(range_1, range_2)
        else:
            damage_dealt = randint(25,50)
            damage_taken = randint(range_1, range_2)

        player_input = input('> ').lower()

        if player_input == "e" and no_estus == True:
            print("The Estus Flask is too far to retrieve.")
            player_health -= damage_taken
        elif player_input == "e" and tarkus == True:
            estus()
            player_health -= damage_taken
            enemy_health -= 30
            print("Tarkus swings for 30 damage.")
        elif player_input == "e":
            estus()
            player_health -= damage_taken
        elif winged_spear == True and tarkus == True:
            enemy_health -= damage_dealt - 30
            print(f"{player_name} strikes for {damage_dealt} damage.", end=' ')
            print("There's an engraving on the weapon:", end=' ')
            print("\"You slimy little wretch! What did I ever do to you?\"")
            print("Tarkus swings for 30 damage.")
        elif winged_spear == True:
            enemy_health -= damage_dealt
            print(f"{player_name} strikes for {damage_dealt} damage.", end=' ')
            print("There's an engraving on the weapon:", end=' ')
            print("\"You slimy little wretch! What did I ever do to you?\"")
        elif tarkus == True:
            enemy_health -= damage_dealt - 30
            print(f"{player_name} strikes for {damage_dealt} damage.")
            print("Tarkus swings for 30 damage")
        elif winged_spear == True:
            enemy_health -= damage_dealt
            print(f"{player_name} strikes for {damage_dealt} damage.", end=' ')
            print("There's an engraving on the weapon:", end=' ')
            print("\"You slimy little wretch! What did I ever do to you?\"")
        else:
            enemy_health -= damage_dealt
            print(f"{player_name} strikes for {damage_dealt} damage.")

        if enemy_health <= 0:
            print("Enemy vanquished!")
            return
        elif enemy_health > 0 and player_input != "e":
            player_health -= damage_taken
            print(enemy_name, f"for {damage_taken} damage.", end=' ')
        else:
            print(enemy_name, f"for {damage_taken} damage.", end=' ')

        if player_health > 0:
            print(f"HP: {int(player_health)}/100")
        else:
            print("HP: 0/100")
            died()

def start():
    global player_name

    player_name = input('Enter name: ')
    print("Press 'E' to use your Estus Flask.")

    player_input = input('> ').lower()

    if player_input == "e":
        print(f"{player_name} drinks from the Estus Flask.", end=' ')
        print("\"Good luck, traveler\"")
        entrance()
    else:
        print("\"Good luck, traveler\"")
        entrance()

def entrance():
    global player_health
    print(f"After having rung the two Bells of Awakening {player_name} finds himself at the entrance to Sen's Fortress.")
    guard = True

    while True:
        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "enter" in player_input or "go" in player_input and guard == True:
            print(f"{player_name} encounters a Serpent Soldier! It looks silly.")
            enemy(snake[0], snake[1], snake[2], snake[3])
            print(f"{player_name} steps through the fortress gates and walks inside.")
            branching_path()
        elif "turn" in player_input or "back" in player_input and guard == True:
            print(f"{player_name} gets struck from behind. It's a Serpent Soldier. It looks silly.")
            player_health /= 2
            print(f"{player_name} takes {int(player_health)} damage. HP: {int(player_health)}/100.")
            enemy(snake[0], snake[1], snake[2], snake[3])
            print(f"There's nothing of importance there. f{player_name} turns back around.")
            guard = False
        elif "turn" in player_input or "back" in player_input and guard == False:
            print("There's nothing of importance there.")
        elif "enter" in player_input or "proceed" in player_input and guard == False:
            print(f"{player_name} steps through the fortress gates and walks inside.")
            branching_path()
        else:
            fog()


def branching_path():
    print("There are three ways to go: Left, straight and right.")

    while True:
        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "left" in player_input:
            branching_path_left()
        elif "right" in player_input:
            branching_path_right()
        elif "straight" in player_input:
            branching_path_straight()
        else:
            fog()


def branching_path_left():
    print(f"The room is dimly lit room. {player_name} proceeds with caution but accidently triggers a pressure plate.", end=' ')
    print("Bolts fire from the front wall.")

    while True:
        player_input = input('> ').lower()

        if player_input == "e":
            print(f"{player_name} takes one last drink before the end. The bolts tear {player_name} to shreds.") #ALTER VALUES
            died()
        elif "roll" in player_input or "evade" in player_input:
            print(f"There are just enough invicibility frames to roll through the bolts.", end=' ')
            print(f"Unfortunately, {player_name} falls through a trap door and crashes into a pit.", end=' ')
            pit()
        elif "block" in player_input or "shield" in player_input:
            print(f"{player_name} doesn't have a shield. The bolts tear {player_name} to shreds.")
            died()
        else:
            fog()

def branching_path_right():
    print(f"{player_name} walks down a long corridor lined with silver plate armor. There's a strange figure off in the distance.")

    while True:
        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "approach" in player_input or "cont" in player_input or "invest" in player_input:
            print(f"{player_name} approaches carefully. The figure turns around. {player_name} encounters a Silver Knight!")
            enemy(s_k[0], s_k[1], s_k[2], s_k[3])
            ambush()
        elif "back" in player_input or "turn" in player_input:
            print(f"{player_name} returns to the enrance.", end=' ')
            branching_path()
        else:
            fog()

def branching_path_straight():
    global player_health

    print(f"{player_name} encounters another Serpent Soldier!")
    enemy(snake[0], snake[1], snake[2], snake[3])
    print(f"{player_name} steps on a pressure plate while playing with the ragdoll physics.", end=' ')
    print(f"Arrows fire from slits in the wall and hit {player_name}.", end=' ')

    player_health -= 50

    if player_health <= 0:
        died()
    else:
        print(f"HP: {int(player_health)}/100.")
        print("There's a rumbling coming from further up ahead . . .")

    while True:
        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "invest" in player_input or "explore" in player_input:
            print(f"{player_name} investigates.")
            break
        else:
            fog()

    print(f"At the end of the room is a doorway leading to a staircase,", end=' ')
    print("and on the adjacent walls are two large tunnels connected by a wide dirt trail.")
    print("The rumbling is coming from one of the tunnels.")

    while True:

        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "door" in player_input or "stair" in player_input:
            second_floor_chest()
        elif "tunn" in player_input or "explore" in player_input:
            print(f"{player_name} goes up the tunnel.")
            second_floor_boulder()
        else:
            fog()

def pit():
    global player_health
    global no_estus

    player_health -= 80

    if player_health <= 0:
        died()
    else:
        print(f"HP: {player_health}/100")
        print("The only way out is via a ladder guarded by a Titanite Demon,", end=' ')
        print("and the ground is covered in a sludge that makes it hard to move.")

    while True:

        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "attack" in player_input or "strike" in player_input:
            print(f"{player_name} confronts the Titanite Demon.")
            enemy(demon[0], demon[1], demon[2], demon[3])
            print(f"{player_name} climbs to the roof of a tower.", end=' ')
            roof_tower()
        elif "sneak" in player_input:
            print(f"{player_name} sneaks past the Titanite Demon and climbs the ladder to the roof of a tower.", end=' ')
            roof_tower()
        elif "run" in player_input or "roll" in player_input:
            print(f"The Titanite Demon knocks {player_name}'s Estus Flask away. The sludge makes it too hard to retrieve.")
            no_estus = True
            enemy(demon[0], demon[1], demon[2], demon[3])
        else:
            fog()


def second_floor_boulder():
    global player_health
    print(f"The rumbling gets louder and louder. There's a giant boulder rolling towards {player_name}.")

    while True:

        player_input = input('> ').lower()

        if player_input == "e":
            estus()
            (f"No amount of health can stand up to a boulder. It crushes {player_name}.")
            died()
        elif "roll" in player_input:
            print(f"{player_name} accidently rolls towards the boulder and gets crushed.")
            died()
        elif "side" in player_input or "step" in player_input:
            print(f"{player_name} avoids getting crushed but takes heavy damage.", end=" ")
            player_health -= 50 # ALTER VALUES
            break
        else:
            fog()

    if player_health <= 0:
        print("HP: 0/100")
        died()
    else:
        print(f"HP: {player_health}/100")
        print(f"{player_name} encounters a Serpent Mage!")
        enemy(mage[0], mage[1], mage[2], mage[3])
        print(f"{player_name} continues up the ramp and into a large room.")
        guillotine()

def second_floor_chest():
    global player_health

    print(f"{player_name} notices a suspicious chest in a room adjoining the staircase.")

    while True:

        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "ignore" in player_input or "leave" in player_input:
            print(f"{player_name} moves on but gets grabbed from behind and split in two.")
            died()
        elif "open" in player_input:
            print(f"{player_name}'s arm is almost chewed off. It's a Mimic!")
            player_health -= 20
            enemy(mimic[0], mimic[1], mimic[2], mimic[3])
            lightning_spear()
        elif "attack" in player_input or "strike" in player_input:
            print(f"{player_name} strikes the chest. Mimic vanquished!", end=' ')
            lightning_spear()
        else:
            fog()


def roof_tower():
    global zweihander
    print("There's someone looking over the parapet.")

    while True:

        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "talk" in player_input or "speak" in player_input:
            print("\"Mmmmmm... Hmm... Mmm... Oh! Pardon me, I was absorbed in thought. I am Siegmeyer of Catarina. What's on your mind, friend?\"")
            print("\"Wait! ...You plan on defeating that Golem?! Fantastic! This knight of Catarina hereby commends you!", end=' ')
            print("Please take this, as a token of my gratitude.\"")
            break
        elif "attack" in player_input or "stab" in player_input or "strike" in player_input:
            print(f"{player_name} backstabs the unsuspecting sightseer. It was a knight from Catarina.")
            berenike_knight()
        else:
            fog()

    while True:
        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "accept" in player_input or "take" in player_input:
            print(f"{player_name} equips the Zweihander.")
            zweihander = True
            print("\"A toast, to your valour. Long may the Sun shine!\"")
            berenike_knight()
        elif "decline" in player_input or "no" in player_input:
            print("\"Understood. But be warned, gallantry entails great risks.\"")
            berenike_knight()
        else:
            fog()


def berenike_knight():
    print("There's a spiral staircase leading to the base of the roof.")

    while True:

        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "down" in player_input or "stair" in player_input:
            print(f"{player_name} encounters a Berenike Knight!")
            enemy(be_k[0], be_k[1], be_k[2], be_k[3])
            pre_golem()
        else:
            fog()

def pre_golem():
    global tarkus
    print(f"{player_name} drops down to a balcony with a bonfire. There's a corridor with a fogged doorway at the end.")

    while True:

        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "traver" in player_input or "enter" in player_input or "fog" in player_input:
            print(f"{player_name} traverses the fog.", end=' ')
            golem()
        elif "summon" in player_input or "tarkus" in player_input:
            print(f"{player_name} summons Iron Tarkus. Together they traverse the fog.", end=' ')
            tarkus = True
            golem()
        else:
            fog()

def ambush():
    global player_health
    print("Something else approaches from behind. It's an ambush!")

    while True:

        player_input = input('> ').lower()

        if "turn" in player_input:
            print(f"Two Serpent Soldiers try to ambush {player_name}.")
            enemy(snake[0], snake[1], snake[2], snake[3])
            print("The other Serpent Soldier takes a swing.")
            damage = player_health // 10
            print(f"Serpent Soldier strikes for {damage} damage. HP: {player_health}/100")
            enemy(snake[0], snake[1], snake[2], snake[3])
            break
        elif "roll" in player_input or "dodge" in player_input:
            print(f"{player_name} dodges the strikes and backstabs one of the two Serpent Soldiers. One left.")
            enemy(snake[0], snake[1], snake[2], snake[3])
            break
        elif "run" in player_input or "flee" in player_input:
            print(f"{player_name} gets ambushed and stabbed to death by two Serpent Soldiers.")
            died()
        else:
            fog()

    print(f"There's an elevator up ahead")

    while True:

        player_input = input('> ').lower()

        if player_input == "e":
            estus()
        elif "take" in player_input or "use" in player_input:
            print(f"{player_name} takes the elvator up to a large room.")
            guillotine()
        else:
            fog()


def lightning_spear():
    print("There's an item in the chest.")
    global lightning_spear

    while True:

        player_input = input('> ').lower()

        if "take" in player_input or "pick" in player_input:
            print(f"{player_name} equips the Lightning Spear and continues up the stairs into a large room.")
            lightning_spear = True
            guillotine()
        elif "pass" in player_input or "leave" in player_input:
            print(f"{player_name} leaves the item behind and continues up the stairs into a large room.")
            guillotine()
        else:
            fog()

def golem():
    print(f"Boss encounter! {player_name} come face to face with a giant iron golem.")
    enemy(boss[0], boss[1], boss[2], boss[3])
    print("\"Congratulations! Off to Anor Londo you go!\"")
    player_input = input().lower()
    exit(0)

def patches():
    global winged_spear
    global lightning_spear
    weapon = False
    treasure = False
    print(f"{player_name} is finally on the fortress roof. There's a man with a friendly smile waving at you.")

    while True:

        player_input = input().lower()

        if player_input == "e":
            estus()
        elif "talk" in player_input or "appro" in player_input:
            print("\"Good day! You look reasonably sane! Care to help me with something?\"")
            treasure = True
            break
        elif  "ignore" in player_input or "keep" in player_input:
            print("He kicks you off a ledge as you turn around.")
            print("\"Heh heh, you got what you deserve! I'll strip your corpse clean! Nyah hah hah hah!\"")
            died()
        elif "attack" in player_input or "strike" in player_input:
            print(f"{player_name} stabs the poor man. He drops his weapon as he collapses to the ground.")
            weapon = True
            break
            pre_golem()
        else:
            fog()

    while weapon == True:

        player_input = input().lower()

        if "take" in player_input:
            print(f"{player_name} equips the Winged Spear.")
            winged_spear = True
            lightning_spear = False
            pre_golem()
        elif "ignore" in player_input or "leave" in player_input:
            pre_golem()
        else:
            fog()

    while treasure == True:

        player_input = input().lower()

        if "yes" in player_input:
            print("\"There's a stash of treasure right down that hole.\"", end=' ')
            print("Go on, have a look. It'll shimmer you blind.\"")
            print(f"{player_name} peaks over the edge only for Patches to kick him off the roof.", end=' ')
            print("\"Heh heh, you got what you deserve! I'll strip your corpse clean! Nyah hah hah hah!\"")
            died()
        elif "no" in player_input:
            print("\"No? Really? Well, that's too bad . . .\"")
            pre_golem()
        else:
            fog()

def guillotine():
    print("At the opposite end of the room is a balcony which leads up to the roof of Sen's Fortress.", end=' ')
    print(f"{player_name} must cross a bridge with two huge guillotines swinging above it to get across.")

    while True:

        player_input = input().lower()

        if player_input == "e":
            estus()
        elif "walk" in player_input:
            print(f"The guilltone cleaves through {player_name}.")
            died()
        elif "run" in player_input:
            print(f"{player_name} makes it across the first guilltone. The second guilltone is swinging at a different speed.")
            break
        elif "roll" in player_input:
            print(f"{player_name} mistimes the roll, takes siginificant damage and is hit with a lightning spell.")
            died()
        else:
            fog()

    while True:

        player_input = input().lower()

        if player_input == "e":
            estus()
        elif "walk" in player_input:
            print(f"The guilltone knocks {player_name} off the bridge.")
            died()
        elif "run" in player_input:
            print(f"{player_name} makes it across the second guillotine and onto the balcony. There's a Serpent Mage!")
            enemy(mage[0], mage[1], mage[2], mage[3])
            patches()
        elif "roll":
            print(f"{player_name} accidently rolls off the bridge.")
            died()
        else:
            fog()

def died():
    print("YOU DIED")
    entrance()

def estus():
    global player_health

    if player_health <= 60:
        player_health += 40
        print(f"{player_name} drinks from the Estus Flask. HP: {player_health}/100")
        return
    elif player_health > 60 and player_health < 100:
        player_health = 100
        print(f"{player_name} drinks from the Estus Flask. HP: {player_health}/100")
        return
    else:
        print(f"{player_name} is at full health.")
        return

def fog():
    print("\"You peer into the fog, in hope of answers.\"")

start()
