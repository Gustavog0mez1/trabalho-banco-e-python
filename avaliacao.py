import random

print("=== AVALIAÇÕES LIVRO ===")
titulo_livro = input("Título do livro: ")
nota_livro = input("Nota do livro: ")
data_avaliacao = input("Data avaliação: ")
perfil_avaliador = input("Perfil avaliador: ")
if not nota_livro.replace('.', '').isdigit():
    print("ERRO: Nota deve conter apenas números!")
else:
    id_avaliacao = random.randint(1, 1000)
    print(f"Avaliação cadastrada! ID:{id_avaliacao} Livro:{titulo_livro} Nota:{nota_livro} Data:{data_avaliacao} Avaliador:{perfil_avaliador}")
