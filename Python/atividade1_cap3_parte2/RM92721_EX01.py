print("Você está digitando as notas dos alunos IMPARES.")
i = 0
total_impares = 0
for i in range(1,50,2):
    nota_aluno = float(input("Digite a nota do aluno {}: ".format(i)))
    total_impares = total_impares + nota_aluno
total_impares = total_impares / 25

print("Você está digitando as notas dos alunos PARES.")
i = 0
total_pares = 0
for i in range(2,51,2):
    nota_aluno = float(input("Digite a nota do aluno {}: ".format(i)))
    total_pares = total_pares + nota_aluno
total_pares = total_pares / 25

print("A média de notas da turma IMPAR é: {}".format(total_impares))
print("A média de notas da turma PAR é: {}".format(total_pares))
if total_pares > total_impares:
    print("A maior média é da turma PAR.")
else:
    print("A maior média é da turma IMPAR.")