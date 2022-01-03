info = list()
dado = list()
while True:
    info.append(str(input('Nome: ')))
    info.append(int(input('Peso: ')))
    dado.append(info[:])
    info.clear()
    resp = \
        str(input('Quer continuar [S/N] ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('Resposta inválida digite [S/N]? ')).upper().strip()
    if resp == 'N':
        break
maior_peso = menor_peso = 0
for pessoa in range(0, len(dado)):
    if pessoa == 0:
        maior_peso = menor_peso = dado[pessoa][1]
    else:
        if dado[pessoa][1] > maior_peso:
            maior_peso = dado[pessoa][1]
        if dado[pessoa][1] < menor_peso:
            menor_peso = dado[pessoa][1]
print(dado)
print(f'Ao todo você cadastrou {len(dado)} pessoas')
print(f'O maior peso foi de {maior_peso}kg. Peso de', end=' ')
for nome in dado:
    if nome[1] == maior_peso:
        print(f' {nome[0]}', end='')
print(f'\nO menor peso foi de {menor_peso}kg. Peso de', end=' ')
for n in dado:
    if n[1] == menor_peso:
        print(f' {n[0]}', end='')






