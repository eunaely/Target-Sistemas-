def inverter_string(s):
    invertida = ''
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

# Exemplo de uso
string_informada = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string_informada)}")
