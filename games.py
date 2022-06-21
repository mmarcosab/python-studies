import guessing
import hangman

print("************************************")
print("            Choose a game           ")
print("************************************")

print("(1) Hangman game", "(2) Guessing game")

jogo = int(input("Enter a game code: "))

if(jogo == 1):
    print("Starting hangman game...")
    hangman.play()
elif(jogo == 2):
    print("Starting guessing game...")
    guessing.play()
