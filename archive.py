arch = open("secret_word.txt", "w") # w sobrescreve o arquivo
arch.write("tests\n")
arch.close()

# write in new lines
arch = open("secret_word.txt", "a")
arch.write("tests\n")
arch.write("tests\n")
arch.close()

arch = open("secret_word.txt", "r") # a para modo leitura
for line in arch:
    print(arch.readline().strip())
arch.close()