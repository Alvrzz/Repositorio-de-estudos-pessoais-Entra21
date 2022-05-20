aluno = str(input('Digite o nome do aluno: '))
m1 = float(input('Digite a primeira nota do aluno: '))
m2 = float(input('Digite a segunda nota do aluno: '))
m3 = float(input('Digite a terceira nota do aluno: '))
media = (m1+m2+m3)/3

dic = dict(aluno=(aluno), media=(media))
print(dic)
#Crie um programa que recebe dados de um aluno como nome e suas notas em supostos 
# 3 trimestres de aula, retornando um novo dicionario como o nome do aluno e a 
# média de suas notas