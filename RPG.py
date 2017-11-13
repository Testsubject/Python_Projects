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
        print ("You have a max or 15 points for stats")
        print("Input the strength of the hero")
        self.strength = int(input("> "))
        print("Input the agility of the hero")
        self.agility = int(input("> "))
        print("Input the intelligence of the hero")
        self.intelligence = int(input("> "))

    def _stat_total(self):
        return sum([self.strength, self.agility, self.intelligence])

def quest_gen(hero):
    print("Your quest can be, slay the dragon, save the princess, or aquire new magic. Which quest do you want?")
    quest = input("1, 2, or 3: ")
    if (quest == "1"):
        print ("Your quest is to slay the dragon.")
    elif (quest == "2"):
        print ("Your quest is to save the princess.")
    elif (quest == "3"):
        print ("Your quest is to aquire new magic.")
    else:
        print ("Please enter 1, 2, or 3.")

def dragon_quest(hero):
    print ("You have 2 options. You can either go to the town for information, or you can head to the dragon's lair.")
    dragon_option1 = input("1 or 2: ")
    if (dragon_option1 == "1"):
        print ("You decide to go to the town for some questions about the dragon.")
        print ("You see a man walking. You decide to talk to him about the dragon.")
        print ("The man said that the dragon comes by to take people to it's lair.")
        print ("Do you ask for more information?")
        ask_man1 = input("1 or 2: ")
        if (ask_man1 == "1"):
            print ("You ask if there are any weaknesses on the dragon.")
            print ("The man said that the dragon usually stays away from cold places.")
            print ("You thank the man for the information and you walk away.")
        if (ask_man1 == "2"):
            print ("You thank the man for the information and you walk away, content with your choice.")
        print ("You notice a magic shop open, do you wish to go to it?")
        shop1 = input("1 or 2: ")
        if (shop1 == "1"):
            print ("You decide to go to the magic shop")
            print ("The man who owns the shop says he has 3 spells for sale.")
            print ("He has Fire, Ice, and Electricity.")
            print ("Do you wish to buy anything? Or leave?")
            shop2 = input("1 or 2: ")
            if (shop2 == "1"):
                print ("You decide to buy something, unfortunatly you only have enough gold to buy one spell.")
                print ("Fire? Ice? or Electricity?")
                shop3 = input("1, 2, or 3: ")
                if (shop3 == "1"):
                    print ("You decide to buy the Fire spell, you hand the man the money.")
                if (shop3 == "2"):
                    print ("You decide to buy the Ice spell, you hand the man the money.")
                if (shop3 == "3"):
                    print ("You decide to buy the Electricity spell, you hand the man the money.")
            if (shop2 == "2"):
                print ("You decide to head towards the dragon's lair.")
        if (shop1 == "2"):
            print ("You decide to head towards the dragon's lair.")
        print ("As you are approaching the dragon's lair, you feel it begin to get warmer.")
        print ("You are at the dragon's lair, you are walking very slowely.")
        print ("It is really hot.")
        print ("You can see the dragon sleeping, you approach it with your sword drawn.")
        rock = random.randint(1,2)
        if (rock == 1):
            print ("You tripped on a rock and the dragon awoke from its slumber.")
            print ("The dragon began to attack you.")
            print ("Do you hide behind a rock? Or attempt to strike it down?")
            dragon_fight1 = input("1 or 2: ")
            if (dragon_fight == "1"):
                print ("You hide behind a rock.")
        if (rock == 2):
            print ("You almost tripped on a rock.")











if __name__ == '__main__':
    hero = Hero()
    quest_gen(hero)
    dragon_quest(hero)

