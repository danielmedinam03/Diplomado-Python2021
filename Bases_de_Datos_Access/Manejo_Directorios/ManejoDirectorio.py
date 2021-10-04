import os
import shutil
from tabulate import tabulate


def menu():
    global opcMenu
    
    opcMenu = input("""Digite la opción que desea realizar:
                  1. Crear Directorio
                  2. Renombrar Directorio
                  3. Copiar Directorio
                  4. Mover Directorio
                  5. Eliminar Directorio 
                  6. Salir
                  Opcion --> """)

    #Validación si es numerico y esta dentro del rango
    if opcMenu.isnumeric() == True :
        opcMenu = int(opcMenu)
        if (opcMenu < 7 and opcMenu > 0):
            #Opcion 1 : Crear Directorio
            if opcMenu==1:

                def crearDirectorio():
                    # Ruta del directorio donde se esta trabajando
                    ruta = os.getcwd()
                    nombreDir = input("Nombre del directorio: ").capitalize()

                    if os.path.exists(nombreDir) == True:
                        print("NOMBRE DEL DIRECTORIO YA EXISTE, PORFAVOR INTENTE CON UNO NUEVO"+"\n")
                        salir = input("Si desea salir digite un * :  ")
                        if salir == "*":
                            print("\nADIOS!!\n")
                            exit()
                        crearDirectorio()

                    else:
                        os.mkdir(ruta + '\\' + nombreDir)
                        lista = os.listdir(r"C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Manejo_Directorios")
                        n=0
                        for i in lista:
                            n +=1
                            print(n,"-",i)
                   
                crearDirectorio()

            #Opcion 2 : Renombrar el directorio
            if opcMenu==2:
                
                def renameDir():
                    #Guarda en una variable los archivos que hay dentro del directorio
                    lista = os.listdir(r"C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Manejo_Directorios")
                    n=0
                    #Recorre uno a uno los directorios 
                    for i in lista:
                        n +=1
                        print(n,"-",i)
                    #Nombre del directorio el cual quiere renombrar
                    nameDir= input("Escriba el nombre del directorio el cual quiere renombrar: ")
                    #Validación de si existe o no el directorio
                    if nameDir in lista:
                        newNameDir = input("Nuevo nombre: ")
                        #Validación para que el renombre no sea existente dentro del directorio
                        if newNameDir in lista:
                            print("Renombralo con un nombre NO EXISTENTE \n")
                            renameDir()
                            exit()
                        else:
                            print()
                        os.rename(nameDir,newNameDir)
                        print("Nombre del directorio ACTUALIZADO, por favor verifica en tu computadora")
                    else:
                        print("El archivo no existe \n")
                        salir = input("\nSi desea salir digite * : ")
                        if salir == "*":
                            print("\nADIOS!!\n")
                            exit()
                        renameDir()
                        
                renameDir()
                
            elif opcMenu==3:
                
                #Funcion copiar directorio
                def copyDir():
                    #Ruta sobre la cual se esta trabajando actualmente
                    ruta = os.getcwd()
                    
                    #Guarda en una variable los archivos que hay dentro del directorio
                    lista = os.listdir(r"C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Manejo_Directorios")
                    n=0
                    #Recorre uno a uno los directorios 
                    for i in lista:
                        n +=1
                        print(n,"-",i)
                    #Nombre de la ruta origen donde esta el directorio
                    nombreRutaOrigen = input("Nombre del directorio para copiar: ")
                    #Nombre de la ruta destino a donde quiere copiar el directorio
                    nombreRutaDestino = input("Nombre del directorio al cual quiere copiar: ")
                    #Validacion que exista el nombre del directorio origen y destino dentro de la lista del directorio padre
                    if (nombreRutaOrigen in lista and nombreRutaDestino in lista) == False:
                        print("""\nNo se encuentra una ruta de origen o una ruta de detino con ese nombre.
                                Por favor intentelo de nuevo.""")
                        salir = input("Si desea salir digite un * : ")
                        if salir == "*":
                            print("\nADIOS!!\n")
                            exit()
                        copyDir()
                    else:
                        rutaOrigen = ruta + "\\" + nombreRutaOrigen
                        rutaDestino = ruta + "\\" + nombreRutaDestino + "\\" + nombreRutaOrigen
                        shutil.copytree(rutaOrigen,rutaDestino)
                        print("Se ha copiado el directorio con exito.")
                    
                copyDir()
                
            elif opcMenu==4:
                def moveDir():
                    #Ruta sobre la cual se esta trabajando actualmente
                    ruta = os.getcwd()
                    #Guarda en una variable los archivos que hay dentro del directorio
                    lista = os.listdir(r"C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Manejo_Directorios")
                    n=0
                    for i in lista:
                        n +=1
                        print(n,"-",i)
                    #Nombre de la ruta origen donde esta el directorio
                    nombreRutaOrigen = input("Nombre del directorio para mover: ")
                    #Nombre de la ruta destino a donde quiere copiar el directorio
                    nombreRutaDestino = input("Nombre del directorio al cual quiere mover: ")
                    #Validacion que exista el nombre del directorio origen y destino dentro de la lista del directorio padre
                    if (nombreRutaOrigen in lista and nombreRutaDestino in lista) == False:
                        print("""\nNo se encuentra una ruta de origen o una ruta de detino con ese nombre.
                                Por favor intentelo de nuevo.""")
                        salir = input("Si desea salir digite un * : ")
                        if salir == "*":
                            print("\nADIOS!!\n")
                            exit()
                        moveDir()
                    else:
                        rutaOrigen = ruta + "\\" + nombreRutaOrigen
                        rutaDestino = ruta + "\\" + nombreRutaDestino + "\\" + nombreRutaOrigen
                        shutil.move(rutaOrigen,rutaDestino)
                        print("""Se ha movido el directorio con exito a la siguiente ruta.
                              --> """,rutaDestino,"\n")
                    
                moveDir()
                
                
            elif opcMenu==5:
                
                def deleteDir():
                    #Guarda en una variable los archivos que hay dentro del directorio
                    lista = os.listdir(r"C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Manejo_Directorios")
                    n=0
                    for i in lista:
                        n +=1
                        print(n,"-",i)
                    #Nombre del directorio a eliminar
                    nombreDirDelete = input("Nombre del directorio que desea eliminar: ")
                    #Validación de si el nombre se encuentra dentro de los archivos del Directorio padre
                    if (nombreDirDelete in lista)==True:
                        lista = os.listdir(r"C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Manejo_Directorios" + "\\" + nombreDirDelete)
                        #print(len(lista))
                        if len(lista) >0:
                            
                            opcEliminar = input("""El directorio contiene archivos...
                                                ¿Desea eliminar de todas formas?
                                                Si o No
                                                --> """).upper()
                            if opcEliminar=="SI":
                                shutil.rmtree(nombreDirDelete)
                            elif opcEliminar=="NO":
                                print("\nADIOS!!\n")
                                exit()
                        else:
                            os.rmdir(nombreDirDelete)
                        print("Directorio eliminado con exito...")
                    else:
                        print("""\nNo se encuentra un Directorio con ese nombre.
                                Por favor intentelo de nuevo.""")
                        salir = input("Si desea salir digite un * : ")
                        if salir == "*":
                            print("\nADIOS!!\n")
                            exit()
                        
                        deleteDir()
                    
                deleteDir()
                       
            elif opcMenu==6:
                print("\nADIOS!!\n")
                exit()
                    
    else:
        print("ERROR!! Digite una de las opciones correspondiente \n")
        menu()
                
menu()          
            
