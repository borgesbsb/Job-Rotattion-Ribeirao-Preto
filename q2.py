# Esta Função verifica se o número pertence à sequência de Fibonacci
def verifica_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False

#Aqui eu posso informar um número ou já defini-lo no código.
num = int(input("Informe um número: "))

fibonacci = [0, 1]
while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if num in fibonacci:
    print(num, "pertence à sequência de Fibonacci!")
else:
    print(num, "não pertence à sequência de Fibonacci.")
