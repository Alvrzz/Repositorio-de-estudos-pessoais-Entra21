#e034.py

contador = 0
soma = 0 
for x in range(1,101):
    if x % 2 !=0:
        soma +=x
        contador +=1
    
print(f'Foram encontrados {contador} numeros impares')
print(f'A soma é de: {soma}')
