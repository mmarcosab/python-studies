print("************************************")
print("********jogo adivinhacao************")
print("************************************")

number = 67
total_retries = 1

while total_retries <= 5:

    print("Tentativa {} de {}".format(total_retries, 5))
    number_two = int(input("Digite um numero: "))

    palpiteMenor = number_two < number
    palpiteMaior = number_two > number
    igual = number == number_two

    if(igual):
        print("acertou")
        control = 1
    else:
        if (palpiteMaior):
            print("voce digitou um valor maior que o esperado")
        elif(palpiteMenor):
            print("voce digitou um valor menor que o esperado")
    total_retries = total_retries + 1

print("Fim de jogo =]")