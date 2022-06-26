
valores = []
print(type(valores))

valores = [1,2,3,4,5,6,7,8,9]
print(valores)

print("Minimal value: ", min(valores))
print("Maximal value: ", max(valores))

print(0 in valores)
print(5 in valores)

valores.append(10)
valores.append(11);
valores.append(12);
print(valores)

valores.remove(11)

print(valores)

print(valores[4])

print("Tamanho da lista: ", len(valores))