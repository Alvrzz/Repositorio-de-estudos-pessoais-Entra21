from datetime import date
data = date.today().year
atual= int(input('Ano de nascimento: '))
idade =  data - atual

if idade == 18:
    print(f'Está na hora de vc ir pro quartel einkkkkkkkk, tu tem {idade}anos')
elif idade<18:
    hm = 18 - idade
    print(f'te falta ainda {hm} anos pra tu se fuderkk')
    print(f'Deu sorte pq tu nasceu em {atual} e tem {idade} anos')
else:
    hm = idade - 18
    print(f'então mano, vo te deita na porrada sacou, ja era pra tu ta no exercito tem {hm} anos')
    