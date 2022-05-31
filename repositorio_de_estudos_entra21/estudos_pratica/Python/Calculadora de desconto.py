n = float(input('Digite o valor do produto: '))
d = float(input('Desconto: '))
val = (n*d)/100
se = n - val
print('---'*30)
print(f'Valor original R${n:.2f} \nCom desconto de {d}% \nDesconto: R${val:.2f}\nValor com desconto: R${se:.2f} ')
print('---'*30)