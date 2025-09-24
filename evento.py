print("=== EVENTO ===")
nome_funcionario = input("Nome do funcionário: ")
nome_evento = input("Nome do evento: ")
data_evento = input("Data do evento: ")

if len(data_evento) > 6 or not data_evento.isdigit():
    print("ERRO: Data deve conter apenas números e no máximo 6 dígitos!")
else:
    id_evento = 1234567890  # ID fixo
    print(f"Evento cadastrado! ID:{id_evento} Funcionário:{nome_funcionario} Evento:{nome_evento} Data:{data_evento}")
