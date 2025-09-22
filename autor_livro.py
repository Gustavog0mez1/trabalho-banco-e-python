import random

print("=== CADASTRO AUTOR LIVRO ===")
nome = input("Nome: ")
data_publicacao = input("Data de publicação: ")
idade = input("Idade: ")
if not idade.isdigit():
    print("ERRO: Idade deve conter apenas números!")
else:
    id_autor = random.randint(1, 1000)
    print(f"Autor cadastrado! ID:{id_autor} Nome:{nome} Data Publicação:{data_publicacao} Idade:{idade}")
