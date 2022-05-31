from datetime import date
atual = date.today().year
pessoas = int(input('Quantas pessoas serão: '))
maior = 0
menor = 0

for c in range(1,pessoas+1):
    ano = int(input(f'qual ano a {c}º pessoa nasceu: '))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'Das {pessoas} pessoas analisadas, {menor} menores e {maior} maiores ')


    
    
      
    
