escolha = input()

# any() retorna True se "boa" for igual a qualquer palavra da lista
if any(palavra.lower() == "boa" for palavra in escolha.split()):
    print("True")
else:
    print("False")