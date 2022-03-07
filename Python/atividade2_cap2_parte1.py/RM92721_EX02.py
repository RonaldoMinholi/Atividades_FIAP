valor_bruto = float(input("Digite o valor bruto: "))
categoria = input("Digite a categoria: (EC - Economica, EX - Executiva e PC - Primeira Classe) ")
viajantes = int(input("Digite a quantidade de viajantes: "))
if (categoria.upper() == "EC") and (viajantes == 2):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.03)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
elif (categoria.upper() == "EC") and (viajantes == 3):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.04)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
elif (categoria.upper() == "EC") and (viajantes >= 4):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.05)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
if (categoria.upper() == "EX") and (viajantes == 2):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.05)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
elif (categoria.upper() == "EX") and (viajantes == 3):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.07)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
elif (categoria.upper() == "EX") and (viajantes >= 4):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.08)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
if (categoria.upper() == "PC") and (viajantes == 2):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.10)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
elif (categoria.upper() == "PC") and (viajantes == 3):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.15)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
elif (categoria.upper() == "PC") and (viajantes >= 4):
    print("Valor bruto: R$ {}".format(valor_bruto))
    desconto = float(valor_bruto * 0.20)
    print("Valor do desconto: R$ {}".format(desconto))
    valor_liquido = valor_bruto - desconto
    print("Valor líquido: R$ {}".format(valor_liquido))
    valor_medio = valor_liquido / viajantes
    print("Valor médio por viajante: R$ {}".format(valor_medio))
