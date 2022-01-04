matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
terceira = 0
segunda = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da matriz na posição [{linha}][{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares = pares + matriz[linha][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end=' ')
    print()
print(f'A soma dos valores pares é {pares}')
for linha in range(0, 3):
    terceira += matriz[linha][2]
print(f'A soma da terceira coluna foi {terceira}')
for coluna in range(0, 3):
    if matriz[1][coluna] > segunda:
        segunda = matriz[1][coluna]
print(f'O maior valor da segunda linha é {segunda}')