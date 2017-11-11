import random

#==> Hero block
class Hero:# All of this can, and probably should, be within a class
    max_stat_total = 15

    def __init__(self):
        self.name = input("Enter the hero's name: ")
        print("Ah, so your name is %s" % (self.name))
        print("Please, tell me your stats...")
        while True:
            self._set_hero_stats()
            print("%s's strength is %s" % (self.name, self.strength))
            print("%s's agility is %s" % (self.name, self.agility))
            print("%s's intelligence is %s" % (self.name, self.intelligence))
            if self._stat_total() <= Hero.max_stat_total:
                break

    def _set_hero_stats(self):
        print("Input the strength of the hero")
        self.strength = int(input("> "))
        print("Input the agility of the hero")
        self.agility = int(input("> "))
        print("Input the intelligence of the hero")
        self.intelligence = int(input("> "))

    def _stat_total(self):
        return sum([self.strength, self.agility, self.intelligence])

def quest_gen(hero):
    quests = ["slay the dragon", "save the princess", "aquire new magic"] #Changed name to quests since it holds multiple quests
    quest = random.choice(quests) #Moved this from the print statement so you can remember the selected quest, similar to how you remember the heros name
    print("Your quest is to %s" % (quest))

    if (quests[0] == quest and hero.strength >= 6): #Checking to see if the selected quest is equal to the dragon quest
        print("You have slain the dragon!")
    elif (quests[1] == quest and hero.agility >= 6):
        print("You haved saved the princess!")
    elif (quests[2] == quest and hero.intelligence >= 6):
        print ("You have gained new magic!")
    else:
        print ("You have failed in your quest.")

if __name__ == '__main__':
    hero = Hero()
    quest_gen(hero)
