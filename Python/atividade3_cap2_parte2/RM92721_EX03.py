segunda = int(input("Digite a quantidade de votos para a segunda-feira: "))
terca = int(input("Digite a quantidade de votos para a terça-feira: "))
quarta = int(input("Digite a quantidade de votos para a quarta-feira: "))
quinta = int(input("Digite a quantidade de votos para a quinta-feira: "))
sexta = int(input("Digite a quantidade de votos para a sexta-feira: "))
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("O dia da semana mais votado é segunda-feira.")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("O dia da semana mais votado é terça-feira.")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("O dia da semana mais votado é quarta-feira.")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("O dia da semana mais votado é quinta-feira.")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("O dia da semana mais votado é sexta-feira.")