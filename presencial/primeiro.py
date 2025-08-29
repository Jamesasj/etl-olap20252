import pandas as pd

vetor = [1, 2, 3, 4, 5]

class MyMath:
    def ehPar(num):
        return num%2 == 0

def ehPar(num):
    return num%2 == 0
for item in vetor:
    if(ehPar(item)):
        print(item)

dados = pd.read_csv("dados.csv")
dados2 = dados[dados['nome']=="João Silva"]

dado3 = dados[["nome", "email"]]

dado3['id'] = dados.index + 1

print(dado3)