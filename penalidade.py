import random

print("===PENALIDADE ===")
titulo_livro = input("Título do livro: ")
data_atraso = input("Data de atraso: ")
nome_cliente = input("Nome do cliente: ")
valor_multa = input("Valor da multa: ")
if not valor_multa.replace('.', '').isdigit():
    print("ERRO: Valor da multa deve conter apenas números!")
else:
    id_penalidade = random.randint(1, 1000)
    print(f"Penalidade cadastrada! ID:{id_penalidade} Livro:{titulo_livro} Data Atraso:{data_atraso} Cliente:{nome_cliente} Multa:R${valor_multa}")
    
