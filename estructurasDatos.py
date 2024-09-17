#Tuplas y listas

#Tuplas: No son modificables = inmutables 'constante'
#Listas: Se permite modificar = mutables 'variable'

#tuplas caracteristica ()

tupla = ('David', 'Billy', 'Adriana', 'Daniel')
print(tupla[0]) #solo permite parametros de lectura

#listas

lista = ['David', 'Billy', 'Adriana', 'Daniel']
lista2 = ['Milton', 'Jose']
lista.extend(lista2)
lista.pop()

lista2d = [
    [
        'David',
        'Martinez',
        '30',
        '30/07/2024'
    ],
    [
        'Adriana',
        'Romero',
        '--',
        '30/07/20--'
    ],
    [
        'Billy',
        'Lozano',
        '--',
        '30/07/20--'
    ]
    ]

#print(lista{0})

print(lista2[1][2])
