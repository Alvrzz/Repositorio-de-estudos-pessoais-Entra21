from random import choice
nome = str(input('Digite seu nome aqui: '))
numero =[1,2,3,4,5,6]
escolhap = choice(numero)
escolha = int(input('Escolha um numero se for diferente do pc tu perde: '))
if escolha == escolhap:
    print(f'Parabens {nome}, você acertou! {escolhap}')
else:
        print(f'Você errou {nome}. A escolha era: {escolhap}!')


