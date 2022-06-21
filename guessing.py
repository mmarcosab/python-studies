import random

def play():
    print("************************************")
    print("           hangman game             ")
    print("************************************")

    #number = 67
    number = round(random.randrange(1, 100))
    total_retries = 1
    max_retries = 5
    points = 1000
    lost_points = 0

    print("Level")
    print("(1) Easy", "(2) Middle", "(3) Hard")
    nivel = int(input("difficult: "))

    if(nivel == 1):
        max_retries = 20
    elif(nivel == 2):
        max_retries = 10
    else:
        max_retries = 5

    for rodada in range(1, max_retries + 1):

        print("Attempt {} de {}".format(total_retries, max_retries))
        number_two = int(input("Enter a number: "))

        smaller = number_two < number
        greater = number_two > number
        equal = number == number_two

        if(equal):
            print("correct!")
            break
        else:
            if (greater):
                print("you entered a value greater than expected")

            elif(smaller):
                print("you entered a value smaller than expected")
        lost_points = number_two - number
        points = abs(points - lost_points)
        total_retries = total_retries + 1

    print("End game =]")
    print("Points: {}".format(points))


