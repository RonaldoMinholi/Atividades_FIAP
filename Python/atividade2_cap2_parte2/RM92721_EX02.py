tipo_assinatura = input("Digite o tipo de assinatura (B - para Basic, S - para Silver, g - para Gold ou P - para Platinum: ")
faturamento_anual = float(input("Digite o valor do faturamento anual: "))
if tipo_assinatura.upper() == "B":
   bonus = float(faturamento_anual) * 0.30
   print("O valor de bônus a ser pago é: R$ {}".format(bonus))
elif tipo_assinatura.upper() == "S":
   bonus = float(faturamento_anual) * 0.20
   print("O valor de bônus a ser pago é: R$ {}".format(bonus))
elif tipo_assinatura.upper() == "G":
   bonus = float(faturamento_anual) * 0.10
   print("O valor de bônus a ser pago é: R$ {}".format(bonus))
elif tipo_assinatura.upper() == "P":
   bonus = float(faturamento_anual) * 0.05
   print("O valor de bônus a ser pago é: R$ {}".format(bonus))