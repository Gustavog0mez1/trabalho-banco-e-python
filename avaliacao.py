import random

print("=== AVALIAÇÕES LIVRO ===")
titulo_livro = input("Título do livro: ")
nota_livro = input("Nota do livro : ")
data_avaliacao = input("Data da avaliação: ")
perfil_avaliador = input("Perfil do avaliador: ")

if not nota_livro.isdigit() or len(nota_livro) > 2:
    print("ERRO: Nota deve conter apenas números e no máximo 2 dígitos!")
else:
    id_avaliacao = random.randint(1, 1000)
    print(f"Avaliação cadastrada! ID:{id_avaliacao} Livro:{titulo_livro} Nota:{nota_livro}/10 Data:{data_avaliacao} Avaliador:{perfil_avaliador}")
    
