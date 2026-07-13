juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}
inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}

#Validacion
def validar_titulo(titulo):
    titulo = titulo.strip()
    if titulo != "":
        return True
    else:
        return False
def validar_codigo(codigo):
    codigo = codigo.upper().strip()
    if codigo == "":
        return False
    if buscar_codigo(codigo, inventario):
        return False
    return True
def validar_clasificacion(clasificacion):
    clasificacion = clasificacion.upper()
    if clasificacion in ["E","T","M"]:
        return True
    else:
        return False
def validar_multiplayer(valor):
    valor = valor.lower()
    return valor in ["s","n"]
def validar_plataforma(plataforma):
    plataforma = plataforma.strip()
    if plataforma != "":
        return True
def validar_genero(genero):
    genero = genero.strip()
    if genero != "":
        return True
def validar_editor(editor):
    editor = editor.strip()
    if editor != "":
        return True
def validar_precio(precio):
    return precio > 0
def validar_stock(stock):
    return stock >= 0
def buscar_codigo(codigo, inventario):
    codigo = codigo.upper()
    return codigo in inventario 

# Funciones Menu
def menu():
    print("========= MENÚ PRINCIPAL =========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("====================================")
def seleccionar_opc():
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion not in [1,2,3,4,5,6]:
            print("Ingrese una opcion válida entre 1 y 6")
            return 0
        else:
            return opcion
    except ValueError:
        print("Debe seleccionar una opción válida")
def stock_plataforma(plataforma, juegos, inventario):
    total = 0
    
    for codigo in juegos:
        if juegos[codigo][1].lower() == plataforma.lower():
            total += inventario[codigo][1]
            print("El total del stock disponibles es:", total)
def busqueda_precio(p_min, p_max, juegos, inventario):
    lista = []
    for codigo in inventario:
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        
        if precio >= p_min and precio <= p_max and stock > 0:
            titulo = juegos[codigo][0]
            
            lista.append(titulo + "--" + codigo)
            lista.sort()
            
            if len(lista) == 0:
                print("No hay juegos en ese rango de precio.")
            else:
                print("Juegos encontrados en ese rango de precio:")
                print(lista)
def actualizar_precio(codigo, nuevo_precio, inventario):
    codigo = codigo.upper()
    
    if buscar_codigo(codigo, inventario):
        inventario[codigo][0] = nuevo_precio
        return True
    return False
def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
    codigo = codigo.upper()
    if buscar_codigo(codigo, inventario):
        return False
    juegos[codigo] = [
        titulo,
        plataforma,
        genero,
        clasificacion.upper(),
        multiplayer,
        editor
        ]
    
    inventario[codigo] = [
        precio,
        stock
    ]
    return True
def eliminar_juego(codigo, juegos, inventario):
    codigo = codigo.upper()
    if buscar_codigo(codigo, inventario):
        del juegos[codigo]
        del inventario[codigo]
        
        return True
    return False

while True:
    menu()
    opcion = seleccionar_opc()
    
    if opcion == 1:
        plataforma = input("Ingrese plataforma a consultar: ")
        stock_plataforma(plataforma, juegos, inventario)
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo: "))
                
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    break
            except:
                print("Debe ingresar valores enteros.")
        busqueda_precio(p_min, p_max, juegos, inventario)
    elif opcion == 3:
        while True:
            codigo = input("Ingrese codigo del juego: ").upper()
            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        break
                except:
                    print("Precio no válido, ingrese nuevamente")
            if actualizar_precio(codigo, nuevo_precio, inventario):
                print("Precio actualizado")
            else:
                print("El código no existe")
            seguir = input("¿Desea actualizar otro precio (s/n)?").lower()
            if seguir == "n":
                break
    elif opcion == 4:
        codigo = input("Ingrese el codigo del juego: ").upper()
        titulo = input("Ingrese el titulo del juego: ")
        plataforma = input("Ingrese la plataforma: ")
        genero = input("Ingrese el genero: ")
        clasificacion = input("Ingrese la clasificacion: ").upper()
        multi = input("¿Tiene multijugador? (s/n)").lower()
        editor = input("ingrese el editor: ")
        
        try:
            precio = input("Ingrese el precio: ")
            stock = input("Ingrese el stock: ")
        except:
            print("Precio y stock deben ser números enteros")
            continue
        
        if not validar_codigo(codigo):
            print("Codigo no válido o ya existe.")
            continue
        if not validar_titulo(titulo):
            print("Titulo no válido o ya existe.")
            continue
        if not validar_plataforma(plataforma):
            print("Plataforma no válida.")
            continue
        if not validar_genero(genero):
            print("Genero no válido.")
            continue
        if not validar_clasificacion(clasificacion):
            print("Clasificacion no válida.")
            continue
        if not validar_multiplayer(multi):
            print("Valor de multiplayer inválido.")
            continue
        if not validar_editor(editor):
            print("Editor inválido.")
            continue
        if not validar_precio(precio):
            print("Precio inválido.")
            continue
        if not validar_stock(stock):
            print("Stock inválido.")
            continue
        
        multiplayer = True if multi == "s" else False
        
        if agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multi, editor, precio, stock, juegos, inventario):
            print("Juego agregado")
        else:
            print("El código ya existe")
    elif opcion == 5:
        codigo = input("Ingrese codigo del juego: ").upper()
        if eliminar_juego(codigo, juegos, inventario):
            print("Juego eliminado")
        else:
            print("El código no existe")
    elif opcion == 6:
        print("Programa finalizado.")
        exit()