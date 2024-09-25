def pertence_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return f"{num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{num} não pertence à sequência de Fibonacci."

# Exemplo de uso
num_informado = int(input("Informe um número: "))
print(pertence_fibonacci(num_informado))
