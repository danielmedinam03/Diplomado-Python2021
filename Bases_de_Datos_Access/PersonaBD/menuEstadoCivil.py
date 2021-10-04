from menu_Table_and_Operaciones import *

from tabulate import*

if menuOpc == 3:

    def menu():

        if menuOpcOperacion == 1:

            print("INSERTAR")
            
            def insert():
                codEstadoCivil = input("Codigo de Estado Civil: ")
                descEstadoCivil = input("Descripcion de Estado Civil: ")

                cursor = conexion.cursor()
                estadoSelect = "SELECT cCodigoEstadoCivil FROM EstadoCivil WHERE cCodigoEstadoCivil=" "'"+codEstadoCivil+"'"
                cursor.execute(estadoSelect)
                rows = cursor.fetchall()
                validacion = rows.__len__()

                if validacion == 0:
                    cursor = conexion.cursor()
                    estadoInsert = "INSERT INTO EstadoCivil(cCodigoEstadoCivil, cDescripcionEstadoCivil) VALUES ('" + \
                    codEstadoCivil.upper()+"','"+descEstadoCivil.upper()+"')"
                    cursor.execute(estadoInsert)
                    cursor.commit()
                    cursor.close()
                    print("\n"+"El registro fue agregado con exito")
                    
                else:
                    print("\n"+"ERROR, no se pudo guardar el registro")
                    insert()
                    
            insert()

        elif menuOpcOperacion == 2:
            print("ACTUALIZAR")

            def menuUpdate():
                opcUpdateEstado = input("""Que campo de la tabla desea actualizar:
                                1. Descripcion estado civil.
                                Opcion #: """)
                if opcUpdateEstado.isnumeric() == True:
                    opcUpdateEstado = int(opcUpdateEstado)
                else:
                    menuUpdate()
                    pass
                return opcUpdateEstado

            if menuUpdate() == 1:

                cursor = conexion.cursor()
                estadoSelect = "SELECT cCodigoEstadoCivil,cDescripcionEstadoCivil FROM EstadoCivil"
                cursor.execute(estadoSelect)
                rows = cursor.fetchall()
                validacion = rows.__len__()
                
                #for i in rows:
                #    print(i)
                    
                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                upDatePK = input(
                    "Ingrese el código de la descripción que desea actualizar: ").upper()

                cursor = conexion.cursor()
                upDateDescripcion = input(
                    "\n"+"Digite la nueva descripcion que desea realizarle al código: ").upper() 
                print("\n")
                upDate = "UPDATE EstadoCivil SET cDescripcionEstadoCivil = '" + \
                    upDateDescripcion+"'WHERE cCodigoEstadoCivil = '"+upDatePK+"'"
                cursor.execute(upDate)
                cursor.commit()
                cursor.close()

                cursor = conexion.cursor()

                cursor = conexion.cursor()
                estadoSelect = "SELECT cCodigoEstadoCivil,cDescripcionEstadoCivil FROM EstadoCivil"
                cursor.execute(estadoSelect)
                rows = cursor.fetchall()
                
                cursor.close()
                
                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                
        elif menuOpcOperacion == 3:
            
            print("ELIMINAR")
            

    menu()
