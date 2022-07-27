anterior = 0
numero = 1
soma = 0
print(anterior)
print(numero)

while numero < 11:
   numero = numero + anterior
   anterior = numero - anterior
   print(numero)
