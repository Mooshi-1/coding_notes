#starting notes to better solidify knowledge of object based programming in python

#create wizard class and simulate magic duels
def main():
    gandalf = Wizard("Gandalf", 30, 50)
    saruman = Wizard("Saruman", 20, 40) 

    def print_status():
        print(f"\n{gandalf.name}: Health={gandalf.health}, Mana={gandalf.mana}")
        print(f"{saruman.name}: Health={saruman.health}, Mana={saruman.mana}\n")
    
    print("The wizard duel begins!")
    print_status()

    try:
        rounds = 2
        for i in range(1, rounds+1):
            if i % 2 == 0:
                gandalf.cast_spell(saruman)
                saruman.cast_spell(gandalf)
                print(f"Round {i} of {rounds} complete.")
                print_status()
            if i % 2 != 0:
                saruman.cast_spell(gandalf)
                gandalf.cast_spell(saruman)
                print(f"Round {i} of {rounds} complete.")
                print_status()
        
    except Exception as e:
        print(e)

class Wizard:
    def __init__(self, name, mana, health):
        self.name = name
        self.mana = mana
        self.health = health
    
    def cast_spell(self, target):
        if self.mana < 10:
            raise Exception(f"{self.name} is out of mana")
        self.mana -=10
        print(f"{self.name} casts fireball on {target.name}")
        target.take_damage()

    def take_damage(self):
        if self.health > 0:
            self.health -= 20
        if self.health <= 0:
            raise Exception(f"{self.name} has been defeated.")


if __name__ == "__main__":
    main()


#continuing lesson
#instance variable -- declared in the CONSTRUCTOR



# # class Wall:
# #     def __init__(self):
# #         self.height = 10

# # south_wall = Wall()
# # south_wall.height = 20 # only updates this instance of a wall
# # print(south_wall.height)
# # # prints "20"

# # north_wall = Wall()
# # print(north_wall.height)
# # # prints "10"

#class variables are declared at the top level of the class definition
#'static variables'

## class Wall():
##      height = 20

# The terms instance and class variable, field, property and attribute are used interchangeably and usually refer to the same concept in languages that support some form of object-oriented programming. Here's a quick reference for some popular languages:
# Language  	Class variable 	Instance variable
# Python 	    Class variable 	Instance variable
# Go 	        Field 	           Field
# JavaScript 	Property 	Property
# C#            Static field 	Field
# Java 	        Static field 	Field


# so class variable - the one defined at the top level of a class definition,
# 