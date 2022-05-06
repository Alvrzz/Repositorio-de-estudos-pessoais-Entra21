maioridade = 18
idade = int(input('digite sua idade: '))
anos = maioridade - idade

if idade >=18:
    print(f'Você ja é maior de idade, você tem {idade} anos.')

elif idade <18:
    print(f'Falta {anos} anos pra você atingir a maioridade')

