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

print(f'Ao todo você cadastrou {len(dado)} pessoas')
print(f'O maior peso foi de {maior_peso}kg. Peso de', end=' ')
cont = c = 0
m_peso = list()
me_peso = list()
for name in dado:
    if maior_peso == name[1]:
        m_peso.append(name[:])
        name.clear()

for c, name in enumerate(m_peso):
    print(f'{name[0]}'.upper(), end='')
    if c < len(m_peso)-2:
        print(',', end=' ')
    if c == len(m_peso)-2:
        print(' e ')
    if c == len(me_peso)-1:
        print('.')

print(f'\nO menor peso foi de {menor_peso}kg. Peso de', end=' ')
for c, name in enumerate(dado):
    print(f'{name[0]}'.upper(), end='')
    if c < len(me_peso) - 2:
        print(',', end=' ')
    if c == len(me_peso) - 2:
        print(' e ')
    if c == len(me_peso)-1:
        print('.')





