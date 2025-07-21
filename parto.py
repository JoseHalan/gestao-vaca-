from datetime import datetime, timedelta

def calcular_parto():
    data_input = input("Informe a data da cobertura da vaca (formato DD/MM/AAAA): ")
    try:
        data_cobertura = datetime.strptime(data_input, "%d/%m/%Y")
        dias_gestacao = timedelta(days=280)  # Tempo médio de gestação
        data_parto = data_cobertura + dias_gestacao
        print(f"A previsão do parto é: {data_parto.strftime('%d/%m/%Y')}")
    except ValueError:
        print("Formato de data inválido! Use DD/MM/AAAA.")

# Executa a função
calcular_parto()