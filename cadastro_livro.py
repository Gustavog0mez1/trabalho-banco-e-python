import random

print("=== CADASTRO LIVRO ===")
titulo = input("Título: ")
valor = input("Valor: ")
estado_conservacao = input("Estado de conservação: ")
autor = input("Autor: ")
if not valor.replace('.', '').isdigit():
    print("ERRO: Valor deve conter apenas números!")
else:
    id_livro = random.randint(1000000000, 9999999999)
    print(f"Livro cadastrado! ID:{id_livro} Título:{titulo} Valor:R${valor} Estado:{estado_conservacao} Autor:{autor}")
