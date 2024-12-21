import os
def ACCOUNT():
    os.system('cls' if os.name == 'nt' else 'clear')
    global NAM
    NAM = input("What is your name? ")
    global PASSis
    PASSis = input("What should your password be? ")
    os.system('cls' if os.name == 'nt' else 'clear')
    VerfPass = input("Verify your password? ")
    if VerfPass == PASSis:
        import Launcher1
        Launcher1
    elif VerfPass != PASSis:
        print("Password is not correct.")
        ACCOUNT()
ACCOUNT()
