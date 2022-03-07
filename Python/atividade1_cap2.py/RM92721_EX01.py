bpm = int(input("Digite a quantidade de batimentos por minuto (BPM): "))
idade = int(input("Digite sua idade: "))
if (idade <= 2) and (bpm >= 120) and (bpm <= 140):
    print("O seu BPM está DENTRO da faixa adequada.")
elif (idade <= 2) and (bpm < 120):
    print("O seu BPM está ABAIXO da faixa adequada.")
elif (idade <= 2) and (bpm > 140):
    print("O seu BPM está ACIMA da faixa adequada.")
elif (idade >= 8) and (idade <= 17) and (bpm < 80):
    print("O seu BPM está ABAIXO da faixa adequada.")
elif (idade >= 8) and (idade <= 17) and (bpm >= 80) and (bpm <=100):
    print("O seu BPM está DENTRO da faixa adequada.")
elif (idade >= 8) and (idade <= 17) and (bpm > 100):
    print("O seu BPM está ACIMA da faixa adequada.")
elif (idade >= 18) and (idade <= 65) and (bpm < 70):
    print("O seu BPM está ABAIXO da faixa adequada.")
elif (idade >= 18) and (idade <= 65) and (bpm >= 70) and (bpm <=80):
    print("O seu BPM está DENTRO da faixa adequada.")
elif (idade >= 18) and (idade <= 65) and (bpm > 80):
    print("O seu BPM está ACIMA da faixa adequada.")
elif (idade > 65) and (bpm >= 50) and (bpm <= 60):
    print("O seu BPM está DENTRO da faixa adequada.")
elif (idade > 65) and (bpm < 50):
    print("O seu BPM está ABAIXO da faixa adequada.")
elif (idade > 65) and (bpm > 60):
    print("O seu BPM está ACIMA da faixa adequada.")
else:
    print("Valor fora da faixa.")

"O seu BPM está DENTRO da faixa adequada."
"O seu BPM está ACIMA da faixa adequada."
"O seu BPM está ABAIXO da faixa adequada."