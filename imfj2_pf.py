# Projeto Final (A) de IMFJ2
# 2º Semestre 2019/2020
# André Santos 21901767

# Strings
TXT_MENU = """
What problem do you want to solve?
1. Floatation
2. Springs

(help): You can type in <quit> at any time to close the program 
        or <menu> to return to this menu.
"""
TXT_FLOAT = """
Current simulation parameters: 
Object: Mass = {0} kg | Density = {1} kg/m^3 | Volume = {2} m^3
Environment: Fluid Density = {3} kg/m^3 | Gravity = {4}

Object would float at: {5}

(help): Type <help> for additional information.
"""
TXT_HELP_FLOAT = """
(help): Typing <set fluid 5> updates the fluid density to 5. 
        Typing <set volume 10, gravity 15> updates both volume and  
        gravity simultaneously. 
        
        !! You are only allowed to change up to 2 object related 
        parameters (mass/density/volume) at a time !!

        You can also type <menu> to return to the main menu or 
        <quit> to close the program.
"""

# Menu
def menu():
    print(TXT_MENU)

    # Waits for user to input one of the options
    user_i = ""
    while (user_i != "quit"):
        user_i = input(">> ")
        user_i = user_i.strip().lower()

        if (user_i[0] == "1" or user_i == "floatation"):
            floatation()

        elif (user_i[0] == "2" or user_i == "springs"):
            springs()

        elif (user_i == "menu"):
            print(TXT_MENU)

        else:
            continue

def floatation():
    mass = 250
    density = 500
    volume = 0.5
    fluid = 1000
    gravity = 9.81
    depth = 0

    user_i = ""
    while True:
        print(TXT_FLOAT.format(mass, density, volume, fluid, gravity, depth))
        
        user_i = input(">> ")
        user_i = user_i.strip().lower().split()

        if (user_i[0] == "set"):
            if (user_i[1] == "mass"):
                mass = user_i[2]

        elif (user_i[0] == "help"):
            print(TXT_HELP_FLOAT)

        elif (user_i[0] == "menu"):
            menu()

        elif (user_i[0] == "quit"):
            exit()

def springs():
    print("springs option")

# Program starts running here
menu()