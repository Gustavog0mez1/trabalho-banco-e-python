import random

print("=== EMPRÉSTIMO LIVRO ===")
titulo_livro = input("Título do livro: ")
estado_livro = input("Estado do livro: ")
data_emprestimo = input("Data do empréstimo : ")
data_emprestimo = input("Data de devoluçao: ")

if len(data_emprestimo) != 6 or not data_emprestimo.isdigit():
    print("ERRO: Data deve conter apenas números e exatamente 6 dígitos!")
else:
    id_emprestimo = random.randint(1000000000, 9999999999)
    data_devolucao = data_emprestimo
    print(f"Empréstimo cadastrado! ID:{id_emprestimo} Livro:{titulo_livro} Estado:{estado_livro} Data Empréstimo:{data_emprestimo} Data Devolução:{data_devolucao}")
