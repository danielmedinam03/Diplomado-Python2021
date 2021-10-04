import pyodbc
from tabulate import tabulate
#import os
from os import getcwd

#Dirección donde se encuentran los archivos
direccion = getcwd()
#Drivers de access
driver = "Microsoft Access Driver (*.mdb, *.accdb)"
print(direccion)
#Cadena de conexión
cadena = (r'DRIVER={};DBQ={}\Discos.accdb;').format(driver,direccion)
#Conexion a ACCESS
conn = pyodbc.connect(cadena)

#Menú de Genero musical para escoger la opción que desea realizar

def menuGeneroMusical():
    menuOpcOperacion = input("""Que operacion desea realizar: 
                       1. Ingresar
                       2. Eliminar
                       Opcion: """)
    #Validación de si es numerico y si esta dentro del rango
    if menuOpcOperacion.isnumeric() == True and (menuOpcOperacion < "3" and menuOpcOperacion > "0"):
        menuOpcOperacion = int(menuOpcOperacion)
        
        #Opcion insertar 1
        
        if menuOpcOperacion == 1:

            print("INSERTAR")
            #Menú insertar 
            def insertGeneroMusical():
                
                codGenero = input("Codigo Genero Musical: ")
                descGenero = input("Nombre del Genero Musical: ")
                cursor = conn.cursor()
                generoSelect = "SELECT cIdGeneroMusical FROM GeneroMusical WHERE cIdGeneroMusical=" "'"+codGenero+"'"
                cursor.execute(generoSelect)
                rows = cursor.fetchall()
                validacion = rows.__len__()

                #validación si esta o no el código
                if validacion == 0:
                    cursor = conn.cursor()
                    
                    #Insert de código y nombre de genero
                    generoInsert = "INSERT INTO GeneroMusical(cIdGeneroMusical, cNombreGenero) VALUES ('" + \
                        codGenero.upper()+"','"+descGenero.upper()+"')"
                    cursor.execute(generoInsert)
                    cursor.commit()
                    cursor.close()
                    print("\n"+"El registro fue agregado con exito")
                    cursor = conn.cursor()
                    
                    # Select para mostrar que se registro el registro
                    generoSelect = "SELECT cIdGeneroMusical,cNombreGenero FROM GeneroMusical"
                    cursor.execute(generoSelect)
                    rows = cursor.fetchall()
                    
                    #Impresion de la tabla
                    print(tabulate(rows, headers=["Codigo", "Descripcion"]))

                else:
                    print("\n"+"ERROR, no se pudo guardar el registro")
                    insertGeneroMusical()

            insertGeneroMusical()

        #Opcion Eliminar
        elif menuOpcOperacion==2:
            print("ELIMINAR")

            #Función DELETE
            def deleteGeneroMusical():
                cursor = conn.cursor()

                #Se hace una seleccion para ver cuales son los registros dentro de la tablas
                Select = "SELECT cIdGeneroMusical,cNombreGenero FROM GeneroMusical"
                cursor.execute(Select)
                rows = cursor.fetchall()
                cursor.close()
                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                deleteCodigo = input("\n"+"Digite el código que desea eliminar de la tabla: ").upper()
                cursor = conn.cursor()
                
                #Operación DELETE
                deleteRegistro = "DELETE FROM GeneroMusical WHERE cIdGeneroMusical=""'" + deleteCodigo + "'"
                cursor.execute(deleteRegistro)
                cursor.commit()
                
                #Se realiza un Select para mostrar por pantalla que se realizo el DELETE
                generoSelect = "SELECT cIdGeneroMusical,cNombreGenero FROM GeneroMusical"
                cursor.execute(generoSelect)
                rows = cursor.fetchall()
                
                #Muestreo de la tabla actualizada con el DELETE
                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                cursor.close()
            deleteGeneroMusical()
    else:
        
        print("ERROR! Ingrese un valor correcto!!")
        menuGeneroMusical()


menuGeneroMusical()