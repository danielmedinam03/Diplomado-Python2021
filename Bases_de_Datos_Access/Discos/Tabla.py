import pyodbc
from tabulate import tabulate
#import os
from os import getcwd

direccion = getcwd()
print(direccion)
cadena = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=' + direccion + r'\Discos.accdb;')
conn = pyodbc.connect(cadena)


def menuGeneroMusical():
    menuOpcOperacion = input("""Que operacion desea realizar: 
                       1. Ingresar
                       2. Eliminar
                       Opcion: """)

    if menuOpcOperacion.isnumeric() == True and (menuOpcOperacion < "3" and menuOpcOperacion > "0"):
        menuOpcOperacion = int(menuOpcOperacion)
        if menuOpcOperacion == 1:

            print("INSERTAR")

            def insertGeneroMusical():
                codGenero = input("Codigo Genero Musical: ")
                descGenero = input("Nombre del Genero Musical: ")

                cursor = conn.cursor()
                generoSelect = "SELECT cIdGeneroMusical FROM GeneroMusical WHERE cIdGeneroMusical=" "'"+codGenero+"'"
                cursor.execute(generoSelect)
                rows = cursor.fetchall()
                validacion = rows.__len__()

                if validacion == 0:
                    cursor = conn.cursor()
                    generoInsert = "INSERT INTO GeneroMusical(cIdGeneroMusical, cNombreGenero) VALUES ('" + \
                        codGenero.upper()+"','"+descGenero.upper()+"')"
                    cursor.execute(generoInsert)
                    cursor.commit()
                    cursor.close()
                    print("\n"+"El registro fue agregado con exito")

                else:
                    print("\n"+"ERROR, no se pudo guardar el registro")
                    insertGeneroMusical()

            insertGeneroMusical()

        elif menuOpcOperacion==2:

            print("ELIMINAR")

            def deleteGeneroMusical():
                cursor = conn.cursor()

                Select = "SELECT cIdGeneroMusical,cNombreGenero FROM GeneroMusical"
                cursor.execute(Select)
                rows = cursor.fetchall()
                #validacion = rows.__len__()
                cursor.close()
                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                deleteCodigo = input("\n"+"Digite el código que desea eliminar de la tabla: ").upper()

                cursor = conn.cursor()

                deleteRegistro = "DELETE FROM GeneroMusical WHERE cIdGeneroMusical=""'" + deleteCodigo + "'"

                cursor.execute(deleteRegistro)
                cursor.commit()

                generoSelect = "SELECT cIdGeneroMusical,cNombreGenero FROM GeneroMusical"
                cursor.execute(generoSelect)
                rows = cursor.fetchall()
                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                cursor.close()
            deleteGeneroMusical()
    else:
        print("ERROR! Ingrese un valor correcto!!")
        menuGeneroMusical()


menuGeneroMusical()
