from math import *

# DO YOU WANNA EDIT OR JUST VIEW EXAMPLES BELOW?
editing = False

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

# 12 Return statements
def part12():
    def cube(num):
        return num*num*num
        print("not visible after return.")
    rresult = cube(4)
    print(rresult)
    print()

# 13 If statements
def part13():
    is_male = True
    is_tall = False
    if is_male and is_tall:
        print("You are a tall male.")
    elif is_male and not(is_tall):
        print("You are a short male.")
    elif not(is_male) and is_tall:
        print("You are not a male but you are tall.")
    else:
        print("You are neither male or tall or both.")

    print()

# 14 If Comparisons
def part14():
    def max_num(inum1, inum2, inum3):
        if inum1 >= inum2 and inum1 >= inum3:
            return inum1
        elif inum2 >= inum1 and inum2 >= inum3:
            return inum2
        else:
            return inum3

    print(max_num(4, 7, 2))
    def cstring(string1, string2):
        if string1 != string2:
            return "Strings do not match"
        else:
            return "Strings match"
    print(cstring("Halo", "Halo"))
    print()

# 15 Better Calculator
def part15():
    bcnum1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    bcnum2 = float(input("Enter second number: "))

    if op == "+":
        print(bcnum1 + bcnum2)
    elif op == "-":
        print(bcnum1 - bcnum2)
    elif op == "*":
        print(bcnum1 * bcnum2)
    elif op == "/":
        print(bcnum1 / bcnum2)
    else:
        print("Invalid operator.")

    print()

# 16 Dictionaries
def part16():
    monthConversions = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
    }
    print(monthConversions)
    print(monthConversions["Jul"])
    print(monthConversions.get("Frd", "Not a valid key."))

# 17 While loop
def part17():
    i = 1
    while i <= 10:
        print(i)
        i += 1
    print("Done with loop...")

# 18 Guessing game
def part18():
    secret_word = "giraffe"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not(out_of_guesses):
        if guess_count < guess_limit:
            guess = input("Enter a guess: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of guesses, YOU LOSE!")
    else:
        print("You win!")

# 19 For loops
def part19():
    ffriends = ["Ella", "Matti", "Pekka"]

    for letter in "Giraffe":
        print(letter)
    for ffriend in ffriends:
        print(ffriend)
    for index in range(5):
        if index == 0:
            print("First iteration.")
        else:
            print("Not first.")

# 20 Exponent function
def part20():
    print(2**3)
    def raise_to_power(base_num, pow_num):
        eresult = 1
        for index in range(pow_num):
            eresult = eresult * base_num
        return eresult
    print(raise_to_power(3, 4))

# 21 2d lists and nested loops
def part21():
    number_grid = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ],
        [ 0 ]
    ]

    print(number_grid[0][0])
    for row in number_grid:
        for col in number_grid:
            print(col)

# 22 Translator
def part22():
    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter.lower() in "aeiou":
                if letter.isupper():
                    translation = translation + "G"
                else:
                    translation = translation + "g"
            else:
                translation = translation + letter
        return translation
    print(translate(input("Enter a phrase: ")))

# 23 Try except
def part23():
    try:
        val = 10/0
        nmb = int(input("Enter a number: "))
        print(nmb)
    except ZeroDivisionError as err:
        print(err)
    except ValueError:
        print("Invalid Input")

# 24 Read files
def part24():
    employee_file = open("employes.txt", "r")

    print(employee_file.readable())
    print(employee_file.read())
    print(employee_file.readline())
    print(employee_file.readline())
    print(employee_file.readlines())
    print(employee_file.readlines()[1])
    for employee in employee_file.readlines():
        print(employee)

    employee_file.close()

# APP START HERE
if editing:
    # TESTING IN EDITING MODE. PUT PART NUMBER BELOW.
    part24()

else:
    # ONLY RUNNING MODE WITH INPUTS.
    selectnum = ""
    while selectnum != "exit":
        print("WELCOME!")
        print("1. Print")
        print("2. Story with variables")
        print("3. String basics")
        print("4. Number basics")
        print("5. Inputs")
        print("6. Calculator")
        print("7. Mad Libs Game")
        print("8. List Basics")
        print("9. List Functions")
        print("10. Tuples on list")
        print("11. Functions")
        print("12. Return statements")
        print("13. If statements")
        print("14. If comparisons")
        print("15. Better calculator")
        print("16. Dictionary")
        print("17. While loop")
        print("18. Guessing game")
        print("19. For loops")
        print("20. Exponent function")
        print("21. 2D lists and nested loops")
        print("22. Translator")
        print("23. Try except")
        print("24. Read files")
        print()
        print("Write exit to end program.")

        selectnum = input("Select part number from list: ")
        if selectnum == "1":
            part1()
        elif selectnum == "2":
            part2()
        elif selectnum == "3":
            part3()
        elif selectnum == "4":
            part4()
        elif selectnum == "5":
            part5()
        elif selectnum == "6":
            part6()
        elif selectnum == "7":
            part7()
        elif selectnum == "8":
            part8()
        elif selectnum == "9":
            part9()
        elif selectnum == "10":
            part10()
        elif selectnum == "11":
            part11()
        elif selectnum == "12":
            part12()
        elif selectnum == "13":
            part13()
        elif selectnum == "14":
            part14()
        elif selectnum == "15":
            part15()
        elif selectnum == "16":
            part16()
        elif selectnum == "17":
            part17()
        elif selectnum == "18":
            part18()
        elif selectnum == "19":
            part19()
        elif selectnum == "20":
            part20()
        elif selectnum == "21":
            part21()
        elif selectnum == "22":
            part22()
        elif selectnum == "23":
            part23()
        elif selectnum == "24":
            part24()
        else:
            print("ERROR INVALID INPUT.")
