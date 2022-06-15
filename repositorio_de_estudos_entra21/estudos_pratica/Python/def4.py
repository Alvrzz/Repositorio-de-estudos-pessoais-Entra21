from re import I


def contador(i, f, p):
    if p <0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='')
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='')
        print('fim!')


#programa principal
print('-='*30)
print('        Defina a contagem        \n')
print('-='*30)
ini = int(input('Inicio:    '))
fim = int(input('Fim:       '))
pas = int(input('Parametro: '))
contador(ini ,fim , pas)
print('-='*30)