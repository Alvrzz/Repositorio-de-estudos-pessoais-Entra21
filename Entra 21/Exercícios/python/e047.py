def calcula_media(aluno):
    boletim = []
    for i in aluno:        
        mr = round(sum(i['Notas'])/len(i['Notas']), 1)
        boletim.append({'Nome': i['Nome'], 'Media das notas': mr})

        mr2 = round(sum(i['Notas2'])/len(i['Notas2']), 1)
        boletim.append({'Nome2': i['Nome2'], 'Media das notas': mr2})

        mr3 = round(sum(i['Notas3'])/len(i['Notas3']), 1)
        boletim.append({'Nome3': i['Nome3'], 'Media das notas': mr3})

    return boletim

aluno = [{
    'Nome': 'Adriano',
    'Notas': [70.7, 80.9, 90.2],
    'Nome2': 'Luan',
    'Notas2': [98.8, 100.0, 96.0],
    'Nome3': 'Zé',
    'Notas3': [88, 86, 78.0]
}]


bl = (calcula_media(aluno))
print('-='*30)
print(f'{bl}')
print('-='*30)
