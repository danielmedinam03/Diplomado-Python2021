import pyodbc

cadena = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Database1.accdb;')

#CONEXION CON LA BD
conexion= pyodbc.connect(cadena)
Genero = conexion.cursor()
numRegistros = int(input("Digite el numero de registros que desea ingresar: "))
for registro in range(numRegistros):
    #Código del genero
    codGenero = input("Digite el código del genero: " + "\n"
                      "F - Femenino" + "\n"
                      "M - Masculino" + "\n"
                      "Otro - Otro genero"+ "\n"
                      "Código: ")
    #Descripcion dle genero
    descGenero= input(("Digite el código del genero: " + "\n"
                      "Femenino" + "\n"
                      "Masculino" + "\n"
                      "Otro genero"+ "\n"
                      "Descripcion: "))
    
    cGeneroSelect= "SELECT cCodigoGenero FROM Genero WHERE (""'"+codGenero+"'"")"
    Genero.execute(cGeneroSelect)
    rows = Genero.fetchmany()
    print(rows)
    """
    cGeneroInsert = "INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES ('"+codGenero.upper()+"','"+descGenero.upper()+"')"
    #cGeneroInsert2= "INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES (""'"+codGenero+"'","'"+descGenero+"'"")"
    
    
    Genero.execute(cGeneroInsert)
    Genero.commit()
    if registro == numRegistros:
        print("Registros exitosos")        
    else:
        pass
    

Genero.commit()

Genero.close()
"""
conexion.close()
    
    
    