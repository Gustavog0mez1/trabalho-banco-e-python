import random

print("=== MANUTENÇÃO LIVRO ===")
titulo_livro = input("Título do livro: ")
estado_livro = input("Estado do livro: ")
data_manutencao = input("Data da manutenção: ")

if len(data_manutencao) > 6 or not data_manutencao.isdigit():
    print("ERRO: Data deve conter apenas números e no máximo 6 dígitos!")
else:
    id_manutencao = random.randint(1, 1000)
    print(f"Manutenção cadastrada! ID:{id_manutencao} Livro:{titulo_livro} Estado:{estado_livro} Data:{data_manutencao}")
