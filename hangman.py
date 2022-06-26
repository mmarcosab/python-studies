
def play():
    print("************************************")
    print("           hangman game             ")
    print("************************************")

    print("Level")
    print("(1) Easy", "(2) Middle", "(3) Hard")
    level = int(input("difficult: "))

    secret_word = "banana".upper()

    done = False
    right = False

    while(not done and not right):
        attempt = input("Which letter?").upper()
        index = 0
        for letter in secret_word:
            if (attempt == letter):
                print("Find the letter {} in position {}".format(letter, index))
            index = index + 1

    print("Playing...")

    print("End game =]")
    # print("Points: {}".format(points))
