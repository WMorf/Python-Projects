#
# Python: 3
#
# Author: Wesley Morford
#
# Demonstrating hoe to pass variables and return them using
# funtions.




def start (nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    '''
        check if this is a new game or not
        If it is new, get the user's name.
        If it is not new, thank the player for
        playing again and continue with the game.
    '''
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            # How rude of you
            if mean >= 2:
                print("\nThe stranger glares at you \nand you trip them as \nyou walk away...")
            else:
                print("\nThe stranger glares at you \nand storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # call win function if condition valid
        win(nice,mean,name)
    if mean > 2: # call lose function if condition valid
        lose(nice,mean,name)
    else:        # call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)






if __name__ == "__main__":
    start()
