n1 = float(input("Olá, digite sua nota 1:" ))
n2 = float(input("Olá, digite sua nota 2:" ))

media = (n1 + n2)/2

if media >= 7:
    print("Aprovado, parabéns!")
elif media >= 5 and media < 7:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO!")