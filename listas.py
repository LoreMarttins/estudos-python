#estrutura de dados

lista = [1,2,3,4,5,6]

#indexaçao

print(lista[0])

#slices

print(lista[0 : 5 : 2])

#percorrer lista

for elemento in range(len(lista)):
    print("elementos:",lista[elemento])

#tamanho da lista
print("tamnho da lista:",len(lista))

#métodos

lista.append(0)
print("Depois do append: ",lista)

lista.insert(0, 17)
print("Depois do insert",lista)
