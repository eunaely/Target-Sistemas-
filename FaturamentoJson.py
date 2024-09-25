import json

# Exemplo de JSON com faturamento diário
dados_faturamento = '''
{
    "faturamento_diario": [1000, 2000, 0, 1500, 3000, 0, 0, 2500, 1800, 0]
}
'''

# Carregar os dados do JSON
faturamento = json.loads(dados_faturamento)["faturamento_diario"]

# Remover os dias sem faturamento (valor zero)
faturamento_validos = [valor for valor in faturamento if valor > 0]

# Menor e maior valor de faturamento
menor_valor = min(faturamento_validos)
maior_valor = max(faturamento_validos)

# Média de faturamento
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

# Dias com faturamento acima da média
dias_acima_da_media = len([valor for valor in faturamento_validos if valor > media_mensal])

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
