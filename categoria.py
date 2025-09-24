import random

print("=== CATEGORIAS LIVRO ===")
genero_livro = input("Gênero do livro: ")
id_categorias = random.randint(1000000000, 9999999999)

print(f"Categoria cadastrada! ID:{id_categorias} Gênero:{genero_livro}")
