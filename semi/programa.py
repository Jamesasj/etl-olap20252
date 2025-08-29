nome = "João"
minhaLista = [1, 2, 3, 4, 5]

for idx, numero in enumerate(minhaLista):
    print("Número: " + str(numero))


def novaFuncaoSoma(x,y):
    return x+y

print("Soma: " + str(novaFuncaoSoma(5, 10)))

print("Olá, " + nome + "!")