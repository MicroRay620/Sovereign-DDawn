import random
#Needed death point
#Start of player stats
player_hp = 100

#Idea the fist is an attack but its also part of the player
#Idea a Stamina stat
#Idea a defense stat
#Idea a Dodge chance and miss chance
#this is for the fist damage fist = random.randint(8, 10)

#player sword stats
sword = False
sword = 10
shield = False
#End of players stats
#wolf stats needed
#Start ofspider stats
#def spider():
    #global spider_hp
spider_hp = 10
    #global spider_dmg
spider_dmg = random.randint(1, 3)
 #fist deals +1 damage to spider
    #global spider_rng_dmg 
spider_rng_dmg = random.randint(1,3)
#end of spider stats
#Start of the dungeon
print("You walk through through the dense, dark, oak forest. Wolves closely behind you, on a hunt for you.")
print("The hoot of owls and and breaking of twiggs is ringing through your ears.")
print("As you walk out into an opening, going blind for a few moments from the rays of sun in your eyes,")
print("You see mineshaft entrance, the door having some mold from being abandoned for so long.")
enter_dungeon = str(input("Would you like to enter the dungeon? ['y' or 'n'] "))
#entering dungeon if statements
if enter_dungeon == "y":
    print("You open the door, there is a staircase leading down.")
    print("You walk down, and enter a room. On the right wall, there is a chest; infront of you there is an opening leading to a fork.")
    option_one = str(input("Do you go for the chest or go to the opening? ['c' or 'o'] "))
    if option_one == "c":
        print("You recieve a sword!")
        sword = True
    #opening/door if statement
    #start of the spider fight
    while spider_hp >= 1:
        if sword == True:
            weapon = input("do you want to use your fist or sword ['f' or 's'] ")
        else:
            print("You will have to use your fist because you don't have a sword")
            weapon = "f"
        if weapon == "f":#start fist
            fist = random.randint(8, 10)
            crit_fist = random.randint(1,100)
            if crit_fist <= 20:
                fist = fist * 1.5
                fist = int(fist)
        spider_hp -= fist#end fist
        if weapon == "s" and sword == True:
            spider_hp -= sword
        if spider_hp <= 0:
            print("congradulations you killed the spider. You have still have", player_hp, "hp left")
            break
        else:
            spider_dmg = random.randint(1 ,3) 
            crit_spider = random.randint(1,100)
            if crit_spider <= 20:
                spider_dmg = spider_dmg * 2
            player_hp -= spider_dmg
            print(spider_hp)
         #end of the spider fight
    while spider_hp <= 0:
        print("You move onward, drops of water echoing through the catacombs. You encounter a fork.")
        print("One option goes to the right, the other goes forward.")
        option_two = str(input("Which do you choose. ['r' or 'f'] "))
        if option_two == "r":
            print("You walk down the path, a torch illuminating the path.")
            print("You go to the end and reach a chest.")
            open_chest = str(input("Do you open the chest? ['y' or 'n'] "))
            if open_chest == "y":
                print("You open the chest and recieve an iron shield!")
                shield = True
                break
            elif open_chest == "n":
                print("You don't open the chest and you head back.")            
        elif option_two == "f":
            print("You move onward. Seeing a break in the path.")
            #break two
elif enter_dungeon == "n":
    while player_hp <= 0:
        print("You died")
