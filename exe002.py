info = list()
dado = list()
maior_peso = 0
while True:
    info.append(str(input('Nome: ')))
    info.append(int(input('Peso: ')))
    dado.append(info[:])
    info.clear()
    resp = str(input('Quer continuar [S/N]: '))
    while resp not in 'SN':
        resp = str(input('Resposta inválida digite [S/N]: ')).strip().upper()
    if resp == 'S':
        break
    for p in dado:
        if p[1] > maior_peso:
            maior_peso = p[1]
        print(m)
