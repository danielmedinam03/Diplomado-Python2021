import pyodbc

cadena = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\PersonaBD\Database1.accdb;')

conexion= pyodbc.connect(cadena)

generoSelect = "SELECT cCodigoGenero, cDescripcionGenero FROM Genero"

cursor = conexion.cursor()
cursor.execute(generoSelect)
rows=cursor.fetchall()
#print(rows)

lista = []

for i in rows:
    #print(i)
    for x in i:
        #print(x)
        lista.append(x)
        #print(lista)       
        
print(lista)
lista = str(lista).format(",")
archivo = open("Archivo1.txt","w")
archivo.write(lista)
    
