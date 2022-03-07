minuto = int(input("Digite o minuto atual: "))
c = minuto
f = 1
while c > 0:
    f = f * c
    c = c - 1

print("A senha é LIBERDADE{}".format(f))

