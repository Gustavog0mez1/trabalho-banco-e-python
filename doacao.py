import random

print("=== DOAÇÃO LIVROS ===")
titulo_livro = input("Título do livro: ")
valor = input("Valor: ")
estado_livro = input("Estado do livro: ")
data_doacao = input("Data doação : ")
if not valor.replace('.', '').isdigit():
    print("ERRO: Valor deve conter apenas números!")
elif len(data_doacao) != 6 or not data_doacao.isdigit():
    print("ERRO: Data deve ter 6 dígitos (DDMMAA)!")
else:
    id_doacao = random.randint(1000000000, 9999999999)
    print(f"Doação cadastrada! ID:{id_doacao} Livro:{titulo_livro} Valor:R${valor} Estado:{estado_livro} Data:{data_doacao}")
