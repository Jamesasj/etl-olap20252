variavel = 123
variavel_str = "james"

print("ola " + variavel_str)


if variavel > 100:
    print("maior que 100")
else:
    print("menor que 100")


# criar uma lista com 10 palavras aleatorias
lista = ["james", "bond", "007", "python", "java", "c++", "javascript", "html", "css", "ruby"]

for palavra in lista:
    if palavra == "java":
        print("encontrei ma melhor linguagem de todas")
    else:
        print(palavra)
    print("proxima palavra")
print("##################### fim do programa ##########################")


def minha_funcao(parametro1, parametro2):
    print("dentro da funcao")
    print(parametro1)
    print(parametro2)
    return parametro1 + parametro2