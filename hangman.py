

def print_welcome_message():
    print("************************************")
    print("           hangman game             ")
    print("************************************")

    print("Level")
    print("(1) Easy", "(2) Middle", "(3) Hard")
    level = int(input("difficult: "))


def carrega_palavra_secreta():
    arquivo = open("secret_word.txt", "r")
    return arquivo.readline().strip()

def play():
    print_welcome_message()
    secret_word = carrega_palavra_secreta().upper()
    right_letters = ["_" for letter in secret_word]
    errors = 0

    done = False
    right = False

    while(not done and not right):
        print("Playing...")
        attempt = input("Which letter?").upper()
        if(attempt in secret_word):
            index = 0
            for letter in secret_word:
                if (attempt == letter):
                    right_letters[index] = letter
                index = index + 1
            print(right_letters)
            absent_letters = str(right_letters).count("_")
            if(absent_letters == 0):
                done = True
        else:
            errors = errors + 1
            print("Errors", errors)
        if (errors == 6):
            print_looser_message(secret_word)
            break
        elif done == True:
            print_winner_message()
    print("End game =]")
    # print("Points: {}".format(points))

def print_looser_message(secret_word):
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_winner_message():
    print("Congrats!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")