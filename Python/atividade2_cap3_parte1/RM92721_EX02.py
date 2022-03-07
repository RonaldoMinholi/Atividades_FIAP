quantidade_transacoes = int(input("Digite a quantidade de transações efetuadas na data de hoje: "))
i = 1
total_trancacoes = 0
while i <= quantidade_transacoes:
    valor_trancacoes = float(input("Digite o valor da transação número {}: ".format(i)))
    total_trancacoes = float(total_trancacoes) + valor_trancacoes
    media_transacoes = float(total_trancacoes / quantidade_transacoes)
    i = i + 1
print("O valor total gasto pelo usuário é de R$ {}".format(total_trancacoes))
print("O valor médio por transação gasto pelo usuário é de R$ {}".format(media_transacoes))