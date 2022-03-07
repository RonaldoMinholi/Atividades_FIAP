rm = input("Digite seu RM: ")
idade = input("Digite sua idade: ")
if int(idade) >= 18:
    print("Sua participação foi autorizada")
else:
    autorizado = input("Você possui autorização? Digite S para SIM ou N para NAO: ")
    #autorizado = autorizado.upper()
    if autorizado.upper() == "S":
        print("Sua participação foi autorizada, aluno de RM {}.".format(rm))
    else:
        print("Sua participação não foi autorizada.")

pontuacao = input("Insira a pontuação do cliente: ")
pontuacao = int(pontuacao)
if pontuacao >= 1000:
    print("O cliente tem direito a receber mais 3gb na sua franquia de internet!")
elif pontuacao >= 500:
    print("O cliente tem direito a receber mais 1,5gb na dua franquia de internet!")
elif pontuacao >= 200:
    print("O cliente tem direito a receber mais 500mb na sua franquia de internet")
else:
    print("O cliente não receberá bônus.")

import math
a = float(input("Informe o valor de A"))
b = float(input("Informe o valor de B"))
c = float(input("Informe o valor de C"))

delta = b * b - 4 * a * c
if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x2 + {}x + {} = 0, obtivemos os seguintes valores: x1 = {} e x2 = {}".format(a,b,c,x1,x2))
elif delta == 0.0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("Para a equação {}x2 + {}x + {} = 0, obtivemos os seguinte valor: x = {}".format(a,b,c,x))
else:
    print("Para a equação {}x2 + {}x + {} = 0, não existem valores raais para x".format(a,b,c))
