from menu_Table_and_Operaciones import *
from tabulate import*

if menuOpc == 2:

    def menu():

        if menuOpcOperacion == 1:

            print("INSERTAR")
            
            def insert():
                codFormaPago = input("Codigo Pago: ")
                descFormaPago = input("Nombre Forma de Pago: ")

                cursor = conexion.cursor()
                pagoSelect = "SELECT cCodFormaPago FROM FormPago WHERE cCodFormaPago=" "'"+codFormaPago+"'"
                cursor.execute(pagoSelect)
                rows = cursor.fetchall()
                validacion = rows.__len__()

                if validacion == 0:
                    cursor = conexion.cursor()
                    pagoInsert = "INSERT INTO FormPago(cCodFormaPago, cNombreFormaPago) VALUES ('" + \
                    codFormaPago.upper()+"','"+descFormaPago.upper()+"')"
                    cursor.execute(pagoInsert)
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
                opcUpdatePago = input("""Que campo de la tabla desea actualizar:
                                1. Nombre Forma de Pago.
                                Opcion #: """)
                if opcUpdatePago.isnumeric() == True:
                    opcUpdatePago = int(opcUpdatePago)
                else:
                    menuUpdate()
                    pass
                return opcUpdatePago

            if menuUpdate() == 1:

                cursor = conexion.cursor()
                pagoSelect = "SELECT cCodFormaPago,cNombreFormaPago FROM FormPago"
                cursor.execute(pagoSelect)
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
                upDate = "UPDATE FormPago SET cNombreFormaPago = '" + \
                    upDateDescripcion+"'WHERE cCodFormaPago = '"+upDatePK+"'"
                cursor.execute(upDate)
                cursor.commit()
                cursor.close()

                cursor = conexion.cursor()

                cursor = conexion.cursor()
                pagoSelect = "SELECT cCodFormaPago,cNombreFormaPago FROM FormPago"
                cursor.execute(pagoSelect)
                rows = cursor.fetchall()
                
                cursor.close()
                
                print(tabulate(rows, headers=["Codigo", "Descripcion"]))
                
        elif menuOpcOperacion == 3:
            
            print("ELIMINAR")
            

    menu()
