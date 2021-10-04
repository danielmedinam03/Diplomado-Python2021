import pyodbc

#[x for x in pyodbc.drivers() if x.startswith("Microsoft Access Driver")]

#Direccion de la base de datos
cadena = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Database1.accdb;')
#Conexion a la base de datos
conexion= pyodbc.connect(cadena)

#Menu sobr cual tabla desea realizar alguna operacion
def menuIngresoTabla():
    global menuOpc
    menuOpc = input("""Ingrese la tabla de la cual quiere realizar alguna operacion:
                   1. Genero
                   2. Formas de pago
                   3. Estado civil
                   4. Estrato
                   5. Productos
                   6. Tipos de Identificación
                   Opcion #: """)
    if menuOpc.isnumeric()==True:
        menuOpc=int(menuOpc)
        if menuOpc >0 and menuOpc<7: 
            pass
        else:
            menuIngresoTabla()
            pass
    else:
        print("Porfavor digite un numero") 
        menuIngresoTabla()
        pass 
    return menuOpc
menuIngresoTabla()

# Menu de cual operacion desea realizar
def menuIngresoOperacion():
    global menuOpcOperacion
    menuOpcOperacion = input ("""Seleccione que operacion desea realizar
                              1. Insertar
                              2. Actualizar
                              3. Eliminar
                              Opcion #: """)
    if menuOpcOperacion.isnumeric()==True:
        menuOpcOperacion=int(menuOpcOperacion)
        if menuOpcOperacion >0 and menuOpcOperacion<4: 
            pass
        else:
            menuIngresoOperacion()
            pass
        pass
    else:
        print("Por favor Digite un numero")
        menuIngresoOperacion()
        pass
    return menuOpcOperacion

menuIngresoOperacion()



