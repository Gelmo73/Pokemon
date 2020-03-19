import os
import marshal
from colorama import init, Fore
import webbrowser
from playsound import playsound

init()

upath = os.environ['USERPROFILE'] + '/Desktop/'
spath = 'C:/PokemonV2'
archivo = {'Voz': '', 'Listado': []}
pokemons = []
genero = 'Sounds/Chico/'


if not os.path.exists(spath):
    os.mkdir(spath)

if os.path.exists(spath + '/storage.bin'):
    with open(spath + '/storage.bin', 'rb') as f:
        archivo = marshal.load(f)
        pokemons = archivo['Listado']
        genero = archivo['Voz']


def limpiar():
    os.system('cls')

    # print('Que voz desearia escuchar? [1] Chico | [2] Chica: ')
    # playsound(genero + '/Voz.mp3')

    # plop = input().strip()
    # if plop == '1':
    #     genero = 'Sounds/Chico/'
    #     ele = False
    # elif plop == '2':
    #     genero = 'Sounds/Chica/'
    #     ele = False
    # else:
    #     pass


def mostrar(pokemons):
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
        playsound(genero + '/NoRegistros.mp3')

        return
    limpiar()
    playsound(genero + '/Borrar.mp3')

    mostrar(pokemons)

    try:
        print('Escribe el numero de registro a borrar: ')
        playsound(genero + '/RegistrosBorrar.mp3')

        op = int(input()) - 1
    except ValueError:
        print('Opcion no valida...')
        playsound(genero + '/OpcionNoValida.mp3')

        return

    if 0 <= op < len(pokemons):
        mostrarRegistro(pokemons[op])
    else:
        print('Fuera de los limites...')
        playsound(genero + '/LimitesFuera.mp3')
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
            playsound(genero + '/RegistroEliminado.mp3')
            des = False
        elif opt == 'N':
            print('Eliminacion cancelada...')
            playsound(genero + '/EliminacionCancelada.mp3')

            des = False
        else:
            print('Elija una opcion valida')
            playsound(genero + '/OpcionNoValida.mp3')

            input()


def agregar():
    limpiar()

    print('Agregando...')
    playsound(genero + '/Agregar.mp3')
    temp = dict()

    print('Nombre: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/ElNombre.mp3')
    temp['Nombre'] = input()

    print('Fecha de Nacimiento: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/LaFecha.mp3')
    temp['Fecha'] = input()

    print('Tipo: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/ElTipo.mp3')
    temp['Tipo'] = input()

    print('Pais: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/ElPais.mp3')
    temp['Pais'] = input()

    print('Ataques: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/LosAtaques.mp3')
    playsound(genero + '/UnoSalir.mp3')
    temp['Ataques'] = []

    appendAttack = True
    while appendAttack:
        valor = input('Escriba un ataque. [1] para dejar de agregar: ')

        if not valor == '1':
            temp['Ataques'].append(valor)
        else:
            appendAttack = False

    pokemons.append(temp)
    print('Registro agregado')


def agregarExistente(registro):
    limpiar()

    temp = dict()

    print('Nombre: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/ElNombre.mp3')
    temp['Nombre'] = input()

    print('Fecha de Nacimiento: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/LaFecha.mp3')
    temp['Fecha'] = input()

    print('Tipo: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/ElTipo.mp3')
    temp['Tipo'] = input()

    print('Pais: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/ElPais.mp3')
    temp['Pais'] = input()

    print('Ataques: ')
    playsound(genero + '/Escribe.mp3')
    playsound(genero + '/LosAtaques.mp3')
    playsound(genero + '/UnoSalir.mp3')
    temp['Ataques'] = []

    appendAttack = True
    while appendAttack:
        valor = input('Escriba un ataque. [1] para dejar de agregar: ')

        if not valor == '1':
            temp['Ataques'].append(valor)
        else:
            appendAttack = False

    return temp


def modificarAtaque(ataques):

    limpiar()
    for registro in range(0, len(ataques)):
        print(registro + 1, '-', ataques[registro])

    print('[ U ] Modificar un unico ataque')
    playsound(genero + '/U.mp3')

    print('[ T ] Modificar todos los ataques')
    playsound(genero + '/T.mp3')

    print('[ C ] Cancelar Modificacion')
    playsound(genero + '/C.mp3')

    opt = input().upper().strip()

    if opt == 'U':
        des2 = True
        while des2:
            print('Escriba el numero: ')
            playsound(genero + '/RegistrosModificar.mp3')

            try:
                l = int(input()) - 1
            except ValueError:
                print('Opcion no valida...')
                playsound(genero + '/OpcionNoValida.mp3')
                return pokemons['Ataques']

            if not (0 <= l < len(ataques)):
                print('Registro no existente')
                playsound(genero + '/SinRegistros.mp3')
                input()
            else:
                ataques[l] = input(str(l + 1) + ': ')
                return ataques
    elif opt == 'T':
        ataques = []
        appendAttack = True
        playsound(genero + '/Escribe.mp3')
        playsound(genero + '/LosAtaques.mp3')
        playsound(genero + '/UnoSalir.mp3')
        while appendAttack:
            valor = input('Escriba un ataque. [1] para dejar de agregar: ')

            if valor != '1':
                ataques.append(valor)
            else:
                appendAttack = False

        return ataques
    elif opt == 'C':
        return None
    else:
        return '1'


def modificar():

    if len(pokemons) == 0:
        print('Sin registros...')
        playsound(genero + '/NoRegistros.mp3')

        return
    limpiar()
    mostrar(pokemons)

    print('Escriba el numero: ')
    playsound(genero + '/RegistrosModificar.mp3')

    try:
        op = int(input()) - 1
    except ValueError:
        print('Opcion no valida...')
        playsound(genero + '/OpcionNoValida.mp3')
        return

    if 0 <= op < len(pokemons):
        mostrarRegistro(pokemons[op])
    else:
        print('Registro no existente')
        playsound(genero + '/SinRegistros.mp3')
        return

    des = True

    while des:

        print('[ U ] Modificar un unico campo')
        playsound(genero + '/U.mp3')

        print('[ T ] Modificar todo el  registro')
        playsound(genero + '/T.mp3')

        print('[ C ] Cancelar Modificacion')
        playsound(genero + '/C.mp3')

        opt = input().upper().strip()

        print()  # Espaciado

        if opt == 'U':

            des2 = True
            while des2:
                print('Escriba el campo que desee modificar: ')
                playsound(genero + '/CampoModificar.mp3')
                l = input().capitalize().strip()

                if l.find('Fecha') == 0:
                    l = 'Fecha'

                if not l in pokemons[op]:
                    print('Registro no existente')
                    playsound(genero + '/NoRegistros.mp3')
                    input()
                elif l == 'Ataques':
                    des3 = True
                    while des3:
                        change = modificarAtaque(pokemons[op]['Ataques'])
                        if change == '1':
                            print('Elija una opcion valida...')
                            playsound(genero + '/OpcionNoValida.mp3')
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
            playsound(genero + '/OpcionNoValida.mp3')
            input()
            limpiar()
            mostrarRegistro(pokemons[op])


def guardar():
    archivo['Voz'] = genero
    archivo['Listado'] = pokemons
    with open(spath + '/storage.bin', 'wb') as f:
        marshal.dump(archivo, f)
    print('Datos guardados...')
    playsound(genero + '/DatosGuardados.mp3')


def buscar():

    while True:
        print('Buscar por nombre: ')
        textoBuscado = input().lower()
        limpiar()

        encontrados = []
        for registro in pokemons:

            if registro['Nombre'].lower().find(textoBuscado) >= 0:
                encontrados.append(registro)

        if len(encontrados) > 0:
            mostrar(encontrados)
        else:
            print('Ningun registro coicidente')
            playsound(genero + 'SinRegistros.mp3')

        playsound(genero + 'ConRegistros.mp3')
        playsound(genero + 'BuscarOtro.mp3')
        select = input(
            'Se han encontrado estos registros. Seleccione numero de registro. [$b] para volver a buscar: ')

        while not select == '$b':
            try:
                op = int(select) - 1

                if 0 <= op < len(pokemons):
                    return encontrados[op]
                else:
                    print('Fuera de los limites...')
                    playsound(genero + '/FueraLimites.mp3')
                    select = '$b'
                    input()

            except ValueError:
                print('Opcion no valida...')
                playsound(genero + '/OpcionNoValida.mp3')
                select = '$b'
                input()


def exportar():

    if len(pokemons) == 0:
        print('Sin registros...')
        playsound(genero + '/NoRegistros.mp3')
        return

    limpiar()
    mostrar(pokemons)

    pokemon = buscar()
    mostrarRegistro(pokemon)

    with open('pokemon.html', 'r') as f:
        html = f.read()

    ataques = []
    for registro in pokemon['Ataques']:
        tmp = '<p>' + registro + '</p> '

        ataques.append(tmp)

    print(ataques)

    html = html.replace('<!--Nombre-->', pokemon['Nombre'])
    html = html.replace('<!--Tipo-->', pokemon['Tipo'])
    html = html.replace('<!--Fecha-->', pokemon['Fecha'])
    html = html.replace('<!--Pais-->', pokemon['Pais'])
    html = html.replace('<!--Ataques-->', ' '.join(ataques))

    playsound(genero + '/ArchivoNombre.mp3')
    nombre = input('Pongale un nombre: ')
    file = upath + nombre + '.html'

    if os.path.exists(file):
        print('Este archivo ya existe...')
        playsound(genero + '/ArchivoExistente.mp3')
        playsound(genero + '/S.mp3')
        if not input('[S] Para reemplazar').upper().strip() == 'S':
            return

    html = html.replace('<!--name-->', nombre)

    with open(file, 'w') as f:
        f.write(html)
        print(nombre, 'ahora se encuentra en el escritorio')
        playsound(genero + '/Escritorio.mp3')

    playsound(genero + 'A.mp3')
    if input('Escriba [A] si desea visualizar su pokemon inmediatamente: ').upper().strip() == 'A':
        webbrowser.open(file)


def menu():
    limpiar()
    print('COREDEX')
    playsound(genero + '/Bienvenida.mp3')
    playsound(genero + '/Escribe.mp3')

    print('1- Agregar')
    playsound(genero + '/EleccionAgregar.mp3')

    print('2- Modificar')
    playsound(genero + '/EleccionModificar.mp3')

    print('3- Borrar')
    playsound(genero + '/EleccionBorrar.mp3')

    print('4- Guardar')
    playsound(genero + '/EleccionGuardar.mp3')

    print('5- Exportar')
    playsound(genero + '/EleccionExportar.mp3')

    print('6- Salir')
    playsound(genero + '/EleccionSalir.mp3')

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
        exportar()
        input()
        menu()
    elif op == '6':
        pass
    else:
        print('Elija una opcion valida...')
        playsound(genero + '/OpcionNoValida.mp3')

        input()
        menu()


menu()
