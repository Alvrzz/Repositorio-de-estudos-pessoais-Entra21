from time import sleep
nome = str(input('Digite seu nome: '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1+n2+n3+n4)/4 
sleep(1)
print('--'*30)
print('Vamos ver se você passou de ano...')
print('--'*30)
sleep(1)
if media >=6.0:
    sleep(1)
    print(f'Parábens, {nome} você passou de ano! \nSua média foi: {media:.1f}!')
    print('--'*30)
else:
    sleep(1)
    print(f'Infelizmente, {nome} você não passou de ano...\nSua média foi: {media:.1f}\nBURROKK')
    print('--'*30)
print('Fim do programa.')
print('--'*30)