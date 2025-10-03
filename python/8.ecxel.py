import pandas as pd
from openpyxl import load_workbook

def calcular_imc(peso, altura):
    """Calcula o IMC dado o peso (Kg) e altura (m)."""
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc):
    """Classifica o IMC de acordo com as faixas padrão."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Nome do arquivo da planilha 
arquivo = "dados_pessoas.xlsx"

try:
    # Ler a planilha e remover espaços extras nos nomes das colunas
    dados = pd.read_excel(arquivo)
    dados.columns = dados.columns.astype(str).str.strip()

    # Verificar se as colunas necessárias existem
    if not {'Nome', 'Peso', 'Altura'}.issubset(dados.columns):
        print("O arquivo Excel deve conter as colunas: Nome, Peso e Altura.")
    else:
        # Converter para valores numéricos (evita erro com texto)
        dados['Peso'] = pd.to_numeric(dados['Peso'], errors='coerce')
        dados['Altura'] = pd.to_numeric(dados['Altura'], errors='coerce')

        # Remover linhas com valores inválidos
        dados = dados.dropna(subset=['Peso', 'Altura'])

        # Calcular IMC e classificação
        dados['IMC'] = dados.apply(lambda x: calcular_imc(x['Peso'], x['Altura']), axis=1)
        dados['Classificação'] = dados['IMC'].apply(classificar_imc)

        # Sobrescrever a planilha original com os novos dados
        with pd.ExcelWriter(arquivo, engine='openpyxl', mode='w') as writer:
            dados.to_excel(writer, sheet_name="pessoas", index=False)

        print(f"Resultados adicionados ao arquivo '{arquivo}'.")

except FileNotFoundError:
    print(f"Erro: o arquivo '{arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
