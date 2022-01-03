par_impar = [[], []]
lista = list()
for c in range(1, 10):
    info = (int(input(f'Digite o {c}º valor: ')))
    if info % 2 == 0:
        par_impar[0].append(info)
    else:
        par_impar[1].append(info)
print('Os valores PARES digitatos foram ', end='')
for c, v in enumerate(sorted(par_impar[0])):
    print(f'{v}', end='')
    if c <= len(par_impar[0])-3:
        print(', ', end='')
    if c == len(par_impar[0])-2:
        print(' e ', end='')
    if c == len(par_impar[0])-1:
        print('.')
print('Os valores IMPARES digitados foram ', end='')
for c, v in enumerate(sorted(par_impar[1])):
    print(f'{v}', end='')
    if c <= len(par_impar[1])-3:
        print(', ', end='')
    if c == len(par_impar[1])-2:
        print(' e ', end='')
    if c == len(par_impar[1])-1:
        print('.')
