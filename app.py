from math import *

# 1 Print pattern
def part1():
    print('   /|')
    print('  / |')
    print(' /  |')
    print('/___|')
    print()

# 2 Story with variables
def part2():
    character_name = "Tim"
    character_age = 27
    is_male = True
    print("There once was a man named " + character_name + ", ")
    print("he was " + str(character_age) + " years old. ")
    character_name = "David"
    print("He really liked a name " + character_name + ", ")
    print("but he didn't like being " + str(character_age) + ".")
    print("")

# 3 String basics
def part3():
    phrase = "Helsinki Finland"
    print(phrase.lower())
    print(phrase.upper())
    print(phrase.upper().isupper())
    print(len(phrase))
    print(phrase[0])
    print(phrase.index("F"))
    print(phrase.replace("Helsinki", "Vantaa"))
    print("Next\n Line")
    print("Tim \"tmitre187\" Fabritius")
    print("")

# 4 Number basics
def part4():
    my_num = -5
    print(3 * (4 + 5))
    print(10 % 3)
    print(str(my_num) + " is my favorite number")
    print(abs(my_num))
    print(pow(3, 4))
    print(max(2, 4))
    print(min(1, 3))
    print(round(3.2))
    print(floor(3.7))
    print(ceil(3.2))
    print(sqrt(36))
    print()

# 5 Inputs
def part5():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Hello " + name + "! You are " + age)
    print()

# 6 Calculator
def part6():
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result = float(num1) + float(num2)
    print(result)
    print()

# 7 Mad Libs Game
def part7():
    color = input("Enter a color: ")
    plural_noun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")
    print("Roses are " + color)
    print(plural_noun + " are blue")
    print("I love " + celebrity)
    print()

# 8 List basics
def part8():
    friends = ["Kevin", "Caren", "Jim", "Oscar", "Tony"]
    friends[1] = "Mike"
    print(friends)
    print(friends[0])
    print(friends[1:])
    print(friends[1:3])
    print()

# 9 List functions
def part9():
    lucky_numbers = [4, 8]
    friends = ["Kevin", "Caren", "Jim", "Oscar", "Tony"]
    friends.extend(lucky_numbers)
    print(friends)
    friends.append("Eric")
    print(friends)
    friends.insert(1, "Kelly")
    print(friends)
    friends.remove(4)
    friends.remove(8)
    print(friends)
    friends.pop()
    print(friends)
    print(friends.index("Kelly"))
    print(friends.count("Kelly"))
    friends.sort()
    print(friends)
    friends.reverse()
    print(friends)
    friends2 = friends.copy()
    friends.clear()
    print(friends)
    print(friends2)
    print()

# 10 Tuples on list
def part10():
    coordinates = [(4, 5), (7, 8), (3, 4)]
    print(coordinates[0])
    print(coordinates)
    print()

# 11 Functions
def part11():
    def sayhi(fname, fage):
        print("Hello " + fname + ", you are " + str(fage))
    print("Top")
    sayhi("Mike", 35)
    sayhi("Tim", 27)
    print("Bottom")
    print()

# TESTING
part11()
