import random

print("=== PENALIDADE ===")
titulo_livro = input("Título do livro: ")
data_atraso = input("Data de atraso : ")
nome_cliente = input("Nome do cliente: ")
valor_multa = input("Valor da multa: ")
if not valor_multa.replace('.', '').isdigit():
    print("ERRO: Valor da multa deve conter apenas números!")
elif len(data_atraso) != 6 or not data_atraso.isdigit():
    print("ERRO: Data deve conter apenas números e ter 6 dígitos!")
elif not nome_cliente.replace(' ', '').isalpha():
    print("ERRO: Nome do cliente deve conter apenas letras!")
else:
    id_penalidade = random.randint(1000000000, 9999999999)
    print(f"Penalidade cadastrada! ID:{id_penalidade} Livro:{titulo_livro} Data Atraso:{data_atraso} Cliente:{nome_cliente} Multa:R${valor_multa}")
