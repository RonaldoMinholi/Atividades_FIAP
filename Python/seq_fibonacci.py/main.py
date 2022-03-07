n = int(input("Digite um número inteiro: "))
t1 = 0
t2 = 1
t3 = 0

while t3 <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
if t1 == n:
    print("Ação bem sucedida!")
else:
    print("A ação falhou...")