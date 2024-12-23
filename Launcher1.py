from os import close
import os
def Main():
    os.system('cls' if os.name == 'nt' else 'clear')
    from AccountCreation import NAM
    print("Hello " + NAM)
    print("1) Apps 2) Settings")
    TODO = input("What would you like to do? ")
    if TODO == "1":
        print("Choose your app: 1) First app")
        APP = input("Which one? ")
        if APP == "1":
            import App1
            App1
    elif TODO == "2":
        import set
        print("Entering settings")
        set.Main()
Main()
