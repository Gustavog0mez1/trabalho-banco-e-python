import random

print("=== COMPRA LIVRO ===")
titulo_livro = input("Título do livro: ")
data_compra = input("Data da compra (6 números): ")
estado_livro = input("Estado do livro: ")

if len(data_compra) != 6 or not data_compra.isdigit():
    print("ERRO: Data deve conter exatamente 6 números!")
else:
    id_compra = random.randint(1000000000, 9999999999)
    print(f"Compra cadastrada! ID:{id_compra} Livro:{titulo_livro} Data:{data_compra} Estado:{estado_livro}")
