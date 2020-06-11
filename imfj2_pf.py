# Projeto Final (A) de IMFJ2
# 2º Semestre 2019/2020
# André Santos 21901767

TXT_MENU = """
What problem do you want to solve?
1. Floatation
2. Springs

You can type in <quit> at any time to close the program 
or <menu> to return to this menu.
"""

def menu():
    print(TXT_MENU)

    user_i = ""
    while (user_i != "quit"):
        user_i = input(">")
        user_i = user_i.strip().lower()

        if (user_i == ""):
            continue

        elif (user_i[0] == "1" or user_i == "floatation"):
            floatation()

        elif (user_i[0] == "2" or user_i == "springs"):
            springs()

def floatation():
    print("floatation option")

def springs():
    print("springs option")

# Program starts running here
menu()