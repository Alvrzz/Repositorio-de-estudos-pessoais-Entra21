def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoavel'   
        else:
            r['situação'] = 'Ruim'
    return r


#programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)