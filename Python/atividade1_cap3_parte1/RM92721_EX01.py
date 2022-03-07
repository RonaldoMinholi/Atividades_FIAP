total_alimentos_ingeridos = int(input("Digite a quantidade total de alimentos consumidos na data de hoje: "))
i = 1
total_calorias = 0
while i <= total_alimentos_ingeridos:
    calorias = int(input("Digite a quantidade de calorias consumidas do alimento {}: ".format(i)))
    print("Quantidade de calorias do alimento {}: {}".format(i,calorias))
    total_calorias = total_calorias + calorias
    i = i + 1
print("O total de calorias consumidas é: {}".format(total_calorias))