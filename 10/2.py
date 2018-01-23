lista = [1,2,2,1]
ulista = []
for item in lista:
    if lista.count(item) > 1:
        ulista.append(item)
print(ulista)