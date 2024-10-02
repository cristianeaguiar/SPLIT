# variável 
nome_completo = input("Informe seu nome completo: ")

#separa os nomes em uma lista
nome_completo_lista = nome_completo.split(" ")

# capitaliza os nomes e exibe o nome completo na tela
print("Nome completo: ", end="")
for nome in nome_completo_lista:
    print(nome.capitalize() , end=" ")


