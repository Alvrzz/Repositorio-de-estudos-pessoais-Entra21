n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1+n2+n3+n4) / 4
print('-='*30)
print(f'Média do aluno é: {media:.1f}')
if media <7 and media >= 5:
    print(f'O aluno está de recuperação.')
elif media <5:
    print(f'O aluno está reprovado.')
elif media >=7:
    print('O aluno está aprovado.')
print('-='*30)
