import random

name = input("Enter the hero's name: ")
print("Ah, so your name is %s" % (name))
print("Please, tell me your stats...")

#==> Hero block
class RPG:# All of this can, and probably should, be within a class
    def hero_stat_input(hero_str, hero_agi, hero_int):
        print("Input the strength of the hero")
        hero_str = int(input("> "))
        print("Input the agility of the hero")
        hero_agi = int(input("> "))
        print("Input the intelligence of the hero")
        hero_int = int(input("> "))
        return (hero_str, hero_agi, hero_int)

    hero_str = 0
    hero_agi = 0
    hero_int = 0
    hero_str, hero_agi, hero_int = hero_stat_input(hero_str, hero_agi, hero_int)
    print("%s's strength is %s" % (name, hero_str))
    print("%s's agility is %s" % (name, hero_agi))
    print("%s's intelligence is %s" % (name, hero_int))
    #Hero block <--

    def quest_gen():
        quests = ["slay the dragon", "save the princess"] #Changed name to quests since it holds multiple quests
        quest = random.choice(quests) #Moved this from the print statement so you can remember the selected quest, similar to how you remember the heros name
        print("Your quest is to %s" % (quest))

        if (quests[0] == quest): #Checking to see if the selected quest is equal to the dragon quest
            print("yes")
        else:
            print("no")
    quest_gen()
