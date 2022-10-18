def keysAndValues(dicc):
    lista = [[], []]
    for key in dicc.keys():
        lista[0].append(key)

    lista[0].sort()

    for i in lista[0]:
        lista[1].append(dicc[i])
        
    print(lista)


diccionario = {'a':1, 'b':2, 'c':3}
keysAndValues(diccionario)
