n = int(input("Digite o número de termos da sequência de Fibonacci: "))

fibonacci = [1, 1]

for i in range(2, n):
    proximo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)

if n == 1:
    fibonacci = [1]
elif n == 0:
    fibonacci = []

print(f"\nSequência de Fibonacci com {n} termos:")
print(fibonacci)
