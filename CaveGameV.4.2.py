#CAVEGAME
#Import
import random
import pickle
import os
#Introduction
print("--------CaveGame V.4.1----------")
print("Credits - Rhys")
#Name loading
account_name = pickle.load(open( "caveuser1.pickle", "rb" ))
with open("DEVDOC.txt","r+",encoding = 'utf-8') as f: 
        text_document = f.readlines()
if account_name == 'Rhys':
 print("Welcome Rhys. Dev mode active")
 print(text_document)
elif account_name == 'Dev':
        print("Welcome developer. Dev mode active")
        print(text_document)
elif account_name == 'Mannat':
        print("You are not authorised to access this game.")
        quit()
elif account_name == 'Tammana':
 print("You are not authorised to access this game.")
 quit()
elif account_name == 'Yameen':
        print("You are not authorised to access this game - YAMEEN. ")
        quit()
elif account_name == 'CroissantMafia':
 print("Weclome Croissant Disciples. Go to this link for the code: https://github.com/DominionGaming/CaveGame")
else:
  print("Welcome to CaveGame")
#Stats
health = 20
damage = 1.5
points = 0
#PART1
print(account_name, "you are travelling down a cave and come to a fork in the cave. There are two paths - which do you choose?")
guess = int(input("Make a guess"))
tnl1 = random.randint(1,2)
if guess == tnl1:
        print('You survived')
        points = points + 50
elif guess != tnl1:
        print("You found a drakon")
        drakon1_health1 = 6
        drakon1_health2 = drakon1_health1 - damage
        drakon1_damage = 0.5
        health = health - drakon1_damage
        print("Your health is",health, "and the drakon's health is", drakon1_health2)
        health = health - drakon1_damage
        print("The drakon is defeated and your health is", health)
        points = points - 50
elif health == 0:
        print("You lost because your health reached 0!")
        print("These are your final points:", points,)

    #PART2
        print("Well", account_name, "you are travelling down a cave and come to another fork in the cave. There are two paths - which do you choose?")
        guess2 = int(input("Make a guess"))
        tnl2 = random.randint(1,2)
        if guess2 == tnl2:
            print('You survived')
            print("You recieved a combat upgrade. You now deal more damage")
            points = points + 50
            damage = damage + 2
        elif guess2 != tnl2:
            print("A wave of fire rolls through the tunnel. You lose 5 health")
            health = health - 5
            points = points - 50
        elif health == 0:
            print("You lost because your health reached 0!")
            print("These are your final points:", points,)
            quit()
                
    #PART3
            print("Well", account_name, "you are travelling down a cave and come to another fork in the cave. This time there are three paths - which do you choose?")
            guess3 = int(input("Make a guess"))
            tnl3 = random.randint(1,3)
            if guess3 == tnl3:
                print('You survived')
                print("You recieved a health upgrade.")
                health = health + 1.4
                points = points + 50
            elif guess3 != tnl3:
                 print("There was a cave in. You lost")
                 points = points - 50
                 quit()
            elif health == 0:
                print("You lost because your health reached 0!")
                print("These are your final points:", points,)
                quit()
    #PART4
                print("Well", account_name, "you are travelling down a cave and come to another fork in the cave. This time there are three paths - which do you choose?")
                guess4 = int(input("Make a guess"))
                tnl4 = random.randint(1,3)
                if guess4 == tnl4:
                    print('You survived')
                    points = points + 50

                elif guess4 != tnl4:
                  print("You found Cleo. Your damage has been increased but at a cost of some health")
                  health = health - 2
                  damage = damage + 1.4
                  points = points - 50
                elif health == 0:
                    print("You lost because your health reached 0!")
                    print("These are your final points:", points,)
                    quit()
    #PART5
                    print("Well", account_name, "you are travelling down a cave and come to another fork in the cave. This time there are three paths - which do you choose?")
                    guess5 = int(input("Make a guess"))
                    tnl5 = random.randint(1,3)
                    if guess5 == tnl5:
                         print('You survived')
                         print("You got 50 extra points!")
                         points = points + 100
                    elif guees5 != tnl5:
                           print("You encounter a demigorgon")
                           demigorgon1_health1 = 8
                           demigorgon1_damage = 2.5
                           demigorgon1_health2 = demigorgon1_health1 - damage
                           health = health - demigorgon1_damage
                           print("Your health is", health, "and the demigorgon's is", demigorgon1_health2)
                           demigorgon1_health3 = 0
                           health = health - demigorgon1_damage
                           print("The demigorgon is defearted but your health is", health)
                           points = points - 50
                    elif health == 0:
                            print("You lost because your health reached 0!")
                            print("These are your final points:", points,)
                            quit()
                   
    #PART6
                            print("Well", account_name, "you are travelling down a cave and come to another fork in the cave. This time there are three paths - which do you choose?")
                            guess6 = int(input("Make a guess"))
                            tnl6 = random.randint(1,3)
                            if guess6 == tnl6:
                                 print('You survived')
                                 points = points + 50
                                 print("These are your final points:", points," and this is your final health:", health)
                            elif guess6 != tnl6:
                                 print("You fell into a pool of acid. You lost health and extra points")
                                 health = health - 4
                                 points = points - 100
                                 print("These are your final points:", points," and this is your final health:", health)
                            elif health == 0:
                                print("You lost because your health reached 0!")
                                print("These are your final points:", points,)
                     
