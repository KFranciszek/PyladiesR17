def cezar(tekst, przesuniecie):
    lista=list(tekst)
    print(lista)
    listaw=[]
    for i in len(lista):
        char = ord(lista[i])
        listaw=''.join(chr(char-przesuniecie))
    print(listaw)

cezar("abcdefghijk", 3)