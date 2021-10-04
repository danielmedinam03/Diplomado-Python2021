from menu_Table_and_Operaciones import *
from tabulate import*

if menuOpc == 1:

    def menuGenero():

        if menuOpcOperacion == 1:

            print("INSERTAR")

            def insertGenero():
                codGenero = input("Codigo Genero: ")
                descGenero = input("Descripcion de Genero: ")

                cursor = conexion.cursor()
                generoSelect = "SELECT cCodigoGenero FROM Genero WHERE cCodigoGenero=" "'"+codGenero+"'"
                cursor.execute(generoSelect)
                rows = cursor.fetchall()
                validacion = rows.__len__()

                if validacion == 0:
                    cursor = conexion.cursor()
                    generoInsert = "INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES ('" + \
                        codGenero.upper()+"','"+descGenero.upper()+"')"
                    cursor.execute(generoInsert)
                    cursor.commit()
                    cursor.close()
                    print("\n"+"El registro fue agregado con exito")

                else:
                    print("\n"+"ERROR, no se pudo guardar el registro")
                    insertGenero()

            insertGenero()

        elif menuOpcOperacion == 2:
            print("ACTUALIZAR")

            def menuUpdateGenero():
                opcUpdateGenero = input("""Que campo de la tabla desea actualizar:
                                1. Descripcion Genero.
                                Opcion #: """)
                if opcUpdateGenero.isnumeric() == True:
                    opcUpdateGenero = int(opcUpdateGenero)
                else:
                    menuUpdateGenero()
                    pass
                return opcUpdateGenero

            if menuUpdateGenero() == 1:

                cursor = conexion.cursor()
                generoSelect = "SELECT cCodigoGenero,cDescripcionGenero FROM Genero"
                cursor.execute(generoSelect)
                rows = cursor.fetchall()
                validacion = rows.__len__()

                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                upDatePK = input(
                    "Ingrese el código de la descripción que desea actualizar: ").upper()

                cursor = conexion.cursor()
                upDateDescripcion = input(
                    "\n"+"Digite la nueva descripcion que desea realizarle al código: ").upper()
                print("\n")
                upDate = "UPDATE Genero SET cDescripcionGenero = '" + \
                    upDateDescripcion+"'WHERE cCodigoGenero = '"+upDatePK+"'"
                cursor.execute(upDate)
                cursor.commit()
                cursor.close()

                cursor = conexion.cursor()

                cursor = conexion.cursor()
                generoSelect = "SELECT cCodigoGenero,cDescripcionGenero FROM Genero"
                cursor.execute(generoSelect)
                rows = cursor.fetchall()

                cursor.close()

                print(tabulate(rows, headers=["Codigo", "Descripcion"]))

        elif menuOpcOperacion == 3:

            print("ELIMINAR")

            cursor = conexion.cursor()

            Select = "SELECT cCodigoGenero,cDescripcionGenero FROM Genero"
            cursor.execute(Select)
            rows = cursor.fetchall()
            validacion = rows.__len__()
            cursor.close()
            print(tabulate(rows, headers=["Codigo", "Descripcion"]))
            deleteCodigo = input("\n"+"Digite el código que desea eliminar de la tabla: ").upper()
            
            cursor = conexion.cursor()

            deleteRegistro= "DELETE FROM Genero WHERE cCodigoGenero=""'" + deleteCodigo + "'"
            
            cursor.execute(deleteRegistro)
            cursor.commit()
            
            generoSelect = "SELECT cCodigoGenero,cDescripcionGenero FROM Genero"
            cursor.execute(generoSelect)
            rows = cursor.fetchall()
            print(tabulate(rows, headers=["Codigo", "Descripcion"]))
            cursor.close()

    menuGenero()
