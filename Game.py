import random
import time

item = []
option = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                        "witch", "monster"])


def print_pause(message):
    print(message)
    time.sleep(2)

#bcgbvc
def intro():
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                                                  "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your rusty (but not very "
                "effective) sword.")


def cave(item):
    if "the elder wand" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("You walk back to the field.")
        field(item)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("But your eye fell on a strange wand next to a rock")

        print_pause("You have found the elder wand of Antioch Peveril!")
        print_pause("You discard your silly old sword and take "
                    "the elder wand with you.")
        print_pause("You walk back out to the field.")
        item.append("the elder wand")
        print_pause("But before you go to fight "
                    + option +
                    "'s with the elder wand, you must first answer "
                    "some questions to improve your skills to beat the "
                    + option + ".")
        print_pause("Note:")
        print_pause("your score must be more than or equal 10 at least to be ready for the confrontation")
        print_pause("Now answer the magical questions and good luck.")


player_score = 0


def score(item):
    global player_score
    question1 = input("The first question is: Sectumsempra is a curse causes deep, slashing wounds\n "
                      "on the victim's body and is intended to be used as a means of causing serious \n"
                      "harm or even death. discovered by Severus Snape. (true) or (false) ")

    if question1 == "true":
        player_score += 5
        print("The score is:", player_score)
    elif question1 == "false":
        print("The score is:", player_score)
    else:
        print("please enter true or false only")
        score(item)

    question2 = input("The second question is : Expecto patronum spell can avoid "
                      "dementors attacking and protect you but to cast it you need a very strong sad memory ."
                      " (true) or (false)")

    if question2 == "false":
        player_score += 5
        print("The score is:", player_score)
    elif question2 == "true":
        print("The score is:", player_score)
    else:
        print("please enter true or false only")
        player_score = 0
        score(item)

    question3 = input("The third question is : Protego Diabolic is a dark defense spell that "
                      "creates a shield around the caster to protect them from dark magic.(true) or (false) ")
    if question3 == "true":
        player_score += 5
        print("The score is:", player_score)
    elif question3 == "false":
        print("The score is:", player_score)
    else:
        print("please enter true or false only")
        player_score = 0
        score(item)

    question4 = input(" The last question is : How many the unforgiven spells?")

    if question4 == "3":
        player_score += 5
        print("The score is:", player_score)
    else:
        print("The score is:", player_score)

    if player_score < 10:
        print("sorry,you can't fight the" + option + "please try again.")
        player_score = 0
        score(item)
    else:
        print("Now you can fight the" + option + "good luck.")
        field(item)


def house(item):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                "opens and out steps a " + option + ".")
    print_pause("Eep! This is the " + option + "'s house!")
    print_pause("The " + option + " attacks you!")
    if "the elder wand" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a rusty sword.")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if 'the elder wand' in item:
                print_pause("As the " + option + " moves to attack, "
                                                 "you unsheath your elder wand.")
                print_pause("The elder wand of Antioch Peveril is in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("But the " + option + " takes one look at "
                                                  "your new wand , he was afraid and runs away!")
                print_pause("You have rid the town of the " + option + "."
                                                                       " Now,You are the hero of the town!")
                print_pause("Now you can return to your home.")
                print_pause("Congratulations,you won.")
            else:
                print_pause("You do your best...")
                print_pause("but your sword is no match for the "
                            "" + option + ".")
                print_pause("You have been turned into a frog!")
                print_pause("Unfortunately,you lost")
            play_again()
            break
        if choice2 == "2":
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been "
                        "followed.")
            field(item)
            break


def field(item):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)")
        if choice1 == "1":
            house(item)
            break
        elif choice1 == "2":
            cave(item)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    intro()
    field(item)
    score(item)


play_game()
