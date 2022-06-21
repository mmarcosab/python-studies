import random

print("************************************")
print("********jogo adivinhacao************")
print("************************************")

#number = 67
number = round(random.randrange(1, 100))
total_retries = 1
max_retries = 5

print("Dificuldade")
print("(1) Fácil", "(2) Médio", "(3) Difícil")
nivel = int(input("Informe o nível de dificuldade: "))

if(nivel == 1):
    max_retries = 20
elif(nivel == 2):
    max_retries = 10
else:
    max_retries = 5

for rodada in range(1, max_retries + 1):

    print("Tentativa {} de {}".format(total_retries, max_retries))
    number_two = int(input("Digite um numero: "))

    palpiteMenor = number_two < number
    palpiteMaior = number_two > number
    igual = number == number_two

    if(igual):
        print("acertou")
        break
    else:
        if (palpiteMaior):
            print("voce digitou um valor maior que o esperado")
        elif(palpiteMenor):
            print("voce digitou um valor menor que o esperado")
    total_retries = total_retries + 1

print("Fim de jogo =]")
