from math import *

# 1 Tulosta kuvio
print('   /|')
print('  / |')
print(' /  |')
print('/___|')
print()

# 2 Tarina muuttujilla
character_name = "Tim"
character_age = 27
is_male = True
print("There once was a man named " + character_name + ", ")
print("he was " + str(character_age) + " years old. ")
character_name = "David"
print("He really liked a name " + character_name + ", ")
print("but he didn't like being " + str(character_age) + ".")
print("")

# 3 Tekstitoimintoja
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

# 4 Numerotoimintoja
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
