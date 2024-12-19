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

# focus on using variable that look like this 

class Wall:
    def __init__(self):
        self.height = 10

south_wall = Wall()
south_wall.height = 20 # only updates this instance of a wall
print(south_wall.height)
# prints "20"

north_wall = Wall()
print(north_wall.height)
# prints "10"

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
# is called different things in different language. 

# class > instance
# for go - field either way
# generally speaking, move away from class variables. define them within the instance instead
# class is essentially a global variable, can cause issues


class Dragon:

    def __init__(self, element):
        self.element = element
        

    def get_breath_damage(self):
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0


def main():
    first_dragon = Dragon("fire")
    print(
        f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage"
    )

    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(
        f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage"
    )


main()

# fire dragon does 300 damage
# ice dragon does 150 damage


class Employee:
    
    company_name = "Age of Dragons, Inc."
    total_employees = 0
    
    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1

    def get_name(self):
        return f"{self.first_name} {self.last_name}"


# look at the line employee.total_employees -- the class of employee was operated on inside __init__
# In Python, there are two main types of variables in a class:

#     Instance variables (using self.) which are unique to each object
#     Class variables (using ClassName.) which are shared across ALL objects of that class



# self.first_name is used inside the class methods to refer to the current instance's attribute
# employee.first_name is used outside the class when you have a specific instance stored in a variable named employee

# Here's a simple example to illustrate:

class Employee:
    def __init__(self, first_name):
        self.first_name = first_name  # 'self' refers to current instance being created
        
    def print_name(self):
        print(self.first_name)  # 'self' refers to whatever instance called this method

# Outside the class
employee1 = Employee("John")
employee1.first_name  # same value as 'self.first_name' was inside the class
employee1.print_name()  # when this runs, 'self' becomes 'employee1'

# Think of self as a placeholder that automatically becomes whatever instance is being used. If I create another employee:

# employee2 = Employee("Jane")

# When methods run on employee2, self refers to employee2 instead of employee1.

# Does this help explain the relationship between self and instance variables? Would you like to see another example?

#----------------------------------------------------------
#library challenge
#have 2 objects, books and librarys


class Book:
    #define the Book class and give it the attributes
    def __init__(self, title, author):
        self.title = title
        self.author = author

    #allows me to print the Book object as I use it in the library
    def __str__(self):
        return f"{self.title} by {self.author}"
        
class Library:

    #initialize library for user name
    def __init__(self, name):
        self.name = name
        self.all_books = []

    #passing Book object as book. list is appended with an object
    def add_book(self, book):
        self.all_books.append(book)

    #delete from book list
    def remove_book(self, book):
        for i in self.all_books:
            #i is the Book object - contains title and author information
            #compare Book object and Library object
            #print (i)
            if i.title == book.title and i.author == book.author:
                self.all_books.remove(i)    
            
    #take a string
    #compare to author and title
    #return matches from library
    def search_books(self, search_string):
        #create empty list to append matches
        search_matches = []
        
        #self.all_books is assigned to our current object and can be iterated to produce 
        #Book objects from the list of books
        
        for book in self.all_books:
            if (search_string.lower() in book.author.lower() or 
            search_string.lower() in book.title.lower()):
                search_matches.append(book)
        return search_matches

#creating a dictionary of student records

class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        letter_grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = letter_grade

    def get_courses(self):
        return self.__courses



#object based 
## how can I write a Human class that holds the data and simulates the behavior of a real human?
#functional based
## when a human takes a step, what's the new state of the game

#creating and dealing a deck of cards

import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = []
        self.create_deck()
        
    def create_deck(self):
        #create rank suit tuple and append to self.__cards
        for suit in DeckOfCards.SUITS:
            for rank in DeckOfCards.RANKS:
                card = (rank, suit)
                self.__cards.append(card)

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if self.__cards == []:
            return None
        return self.__cards.pop()

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"



#example of inheritence and hierarchys

class RealEstate:
    def __init__(self, location):
        self.__location = location


class Residential(RealEstate):
    def __init__(self, location, bedrooms):
        super().__init__(location)
        self.__bedrooms = bedrooms


class House(Residential):
    def __init__(self, location, bedrooms, yard_size):
        super().__init__(location, bedrooms)
        self.__yard_size = yard_size

    
    #calling on functions set up for a dragon fight

    def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]


    for dragon in dragons:
        describe(dragon)

    #each dragon breathe fire at 3,3 - pass in all other~~ dragons as the unit
    for obj in dragons:    
        dragons_copy = dragons.copy()
        dragons_copy.remove(obj)
        obj.breathe_fire(3,3,dragons_copy)
        


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("====================================")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()


##