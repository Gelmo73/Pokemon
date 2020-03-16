import os
import marshal
from colorama import init, Fore

init()

upath = os.environ['USERPROFILE'] + '/Desktop/'
spath = 'C:/PokemonV2'
pokemons = []


if not os.path.exists(spath):
    os.mkdir(spath)

if os.path.exists(spath + '/storage.bin'):
    with open(spath + '/storage.bin', 'rb') as f:
        pokemons = marshal.load(f)


def limpiar():
    os.system('cls')


def mostrar():
    limpiar()
    for registro in pokemons:

        print(
            Fore.RED, 'Regitro: ', pokemons.index(registro) + 1,
            Fore.WHITE, '\nNombre: ', registro['Nombre'],
            '\nTipo: ', registro['Tipo'],
            '\nPais: ', registro['Pais'],
            '\nFecha de Nacimiento: ', registro['Fecha'],
            '\nAtaques: ', ' | '.join(registro['Ataques'])
        )
        print()


def mostrarRegistro(registro):
    limpiar()

    print(
        'Nombre: ', registro['Nombre'],
        '\nTipo: ', registro['Tipo'],
        '\nPais: ', registro['Pais'],
        '\nFecha de Nacimiento: ', registro['Fecha'],
        '\nAtaques: ', ' | '.join(registro['Ataques'])
    )
    print()


def borrar():
    if len(pokemons) == 0:
        print('Sin registros...')
        return
    limpiar()
    mostrar()

    try:
        op = int(input('Elija el registro a borrar: ')) - 1
    except ValueError:
        print('Opcion no valida...')
        return

    if 0 <= op < len(pokemons):
        mostrarRegistro(pokemons[op])
    else:
        print('Fuera de los limites...')
        return

    des = True
    while des:
        limpiar()
        mostrarRegistro(pokemons[op])

        opt = input(
            'Seguro que desea eliminar este registro [S/N]').upper().strip()

        if opt == 'S':
            pokemons.pop(op)
            print('Reagistro eliminado...')
            des = False
        elif opt == 'N':
            print('Eliminacion cancelada...')
            des = False
        else:
            print('Elija una opcion valida')
            input()


def agregar():
    limpiar()

    print('Agregando...')

    temp = {
        'Nombre': input('Nombre: '),
        'Fecha': input('Fecha de Nacimiento: '),
        'Tipo': input('Tipo: '),
        'Pais': input('Pais: '),
        'Ataques': []
    }

    appendAttack = True
    while appendAttack:
        valor = input('Escriba un ataque. [1] para dejar de agregar: ')

        if valor != '1':
            temp['Ataques'].append(valor)
        else:
            appendAttack = False

    pokemons.append(temp)
    print('Registro agregado')


def agregarExistente(registro):
    limpiar()

    temp = {
        'Nombre': input('Nombre: '),
        'Fecha': input('Fecha de Nacimiento: '),
        'Tipo': input('Tipo: '),
        'Pais': input('Pais: '),
        'Ataques': []
    }

    appendAttack = True
    while appendAttack:
        valor = input('Escriba un ataque. [1] para dejar de agregar: ')

        if valor != '1':
            temp['Ataques'].append(valor)
        else:
            appendAttack = False

    return temp


def modificarAtaque(ataques):

    limpiar()
    for registro in range(0, len(ataques)):
        print(registro + 1, '-', ataques[registro])

    opt = input('''
[ U ] Modificar un unico ataque 
[ T ] Reescribir ataques 
[ S ] Salir de modificacion

''').upper().strip()

    if opt == 'U':
        des2 = True
        while des2:
            l = int(input('Escriba el numero: ')) - 1
            if not (0 <= l < len(ataques)):
                print('Registro no existente')
                input()
            else:
                ataques[l] = input(str(l + 1) + ': ')
                return ataques
    elif opt == 'T':
        ataques = []
        appendAttack = True
        while appendAttack:
            valor = input('Escriba un ataque. [1] para dejar de agregar: ')

            if valor != '1':
                ataques.append(valor)
            else:
                appendAttack = False

        return ataques
    elif opt == 'S':
        return None
    else:
        return '1'


def modificar():

    if len(pokemons) == 0:
        print('Sin registros...')
        return
    limpiar()
    mostrar()

    try:
        op = int(input('Elija el registro a modificar: ')) - 1
    except ValueError:
        print('Opcion no valida...')
        return

    if 0 <= op < len(pokemons):
        mostrarRegistro(pokemons[op])
    else:
        print('Fuera de los limites...')
        return

    des = True

    while des:
        opt = input('''
[ U ] Modificar un unico campo 
[ T ] Modificar todo el  registro 
[ C ] Cancelar Modificacion

''').upper().strip()

        print()  # Espaciado

        if opt == 'U':

            des2 = True
            while des2:
                l = input(
                    'Escriba el campo que desee modificar: ').capitalize().strip()

                if l.find('Fecha') == 0:
                    l = 'Fecha'

                if not l in pokemons[op]:
                    print('Registro no existente')
                    input()
                elif l == 'Ataques':
                    des3 = True
                    while des3:
                        change = modificarAtaque(pokemons[op]['Ataques'])
                        if change == '1':
                            print('Elija una opcion valida...')
                            input()
                        elif change == None:
                            des3 = False
                        else:
                            pokemons[op]['Ataques'] = change

                    des2 = False
                else:
                    pokemons[op][l] = input(l + ': ')
                    des2 = False

            des = False

        elif opt == 'T':
            result = agregarExistente(pokemons[op])
            if not result == 0:
                pokemons[op] = result
                des = False
        elif opt == 'C':
            print('Modificacion cancelada...')
        else:
            print('Opcion no valida')
            input()
            limpiar()
            mostrarRegistro(pokemons[op])


def guardar():
    with open(spath + '/storage.bin', 'wb') as f:
        marshal.dump(pokemons, f)
    print('Datos guardados...')


def menu():
    limpiar()
    print('''
1- Agregar
2- Modificar
3- Borrar
4- Guardar
5- Exportar
6- Salir
    ''')

    op = input('Elija una opcion: ')

    if op == '1':
        agregar()
        input()
        menu()
    elif op == '2':
        modificar()
        input()
        menu()
    elif op == '3':
        borrar()
        input()
        menu()
    elif op == '4':
        guardar()
        input()
        menu()
    elif op == '5':
        pass
    elif op == '6':
        pass
    else:
        print('Debe seleccionar una opcion...')
        input()
        menu()


menu()
