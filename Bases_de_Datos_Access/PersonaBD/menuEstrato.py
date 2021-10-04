from menu_Table_and_Operaciones import *
from tabulate import*

if menuOpc == 4:

    def menu():

        if menuOpcOperacion == 1:

            print("INSERTAR")
            
            def insert():
                codEstrato = input("Codigo Estrato: ")
                descEstrato = input("Descripcion de Estrato: ")

                cursor = conexion.cursor()
                estratoSelect = "SELECT cCodigoEstrato FROM Estrato WHERE cCodigoEstrato=" "'"+codEstrato+"'"
                cursor.execute(estratoSelect)
                rows = cursor.fetchall()
                validacion = rows.__len__()

                if validacion == 0:
                    cursor = conexion.cursor()
                    estratoInsert = "INSERT INTO Estrato(cCodigoEstrato, cDescipcionDelEstrato) VALUES ('" + \
                    codEstrato.upper()+"','"+descEstrato.upper()+"')"
                    cursor.execute(estratoInsert)
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
                opcUpdate = input("""Que campo de la tabla desea actualizar:
                                1. Descripcion Estrato.
                                Opcion #: """)
                if opcUpdate.isnumeric() == True:
                    opcUpdate = int(opcUpdate)
                else:
                    menuUpdate()
                    pass
                return opcUpdate

            if menuUpdate() == 1:

                cursor = conexion.cursor()
                estratoSelect = "SELECT cCodigoEstrato,cDescipcionDelEstrato FROM Estrato"
                cursor.execute(estratoSelect)
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
                upDate = "UPDATE Estrato SET cDescipcionDelEstrato = '" + \
                    upDateDescripcion+"'WHERE cCodigoEstrato = '"+upDatePK+"'"
                cursor.execute(upDate)
                cursor.commit()
                cursor.close()

                cursor = conexion.cursor()

                cursor = conexion.cursor()
                estratoSelect = "SELECT cCodigoEstrato,cDescipcionDelEstrato FROM Estrato"
                cursor.execute(estratoSelect)
                rows = cursor.fetchall()
                
                cursor.close()
                
                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                
        elif menuOpcOperacion == 3:
            
            print("ELIMINAR")
            

    menu()
