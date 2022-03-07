rm = input("Digite seu RM: ")
idade = input("Digite sua idade: ")
if int(idade) >= 18:
    print("Sua participação foi autorizada, aluno de RM {}!".format(rm))
    print("Voce receberá mais informações no e-mail cadastrado")
else:
    print("Sua participação não foi autorizada")
