import os
import openpyxl
import pyodbc

#Ruta
rutaBase = os.getcwd()

cadenaRutaBD=r'C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\PersonaBD\DataBase1.accdb;'
driver = "Microsoft Access Driver (*.mdb, *.accdb)" 
cadena = (r'DRIVER={};DBQ={}').format(driver,cadenaRutaBD)
conexion = pyodbc.connect(cadena)

# Abre un libro de excel
excel_document = openpyxl.load_workbook(rutaBase + '\EstadoCivil.xlsx')

libro="EstadoCivil.xlsx"

# Ingreso al contenido de una libro de excel
sheet = excel_document['DanielEstadoCivil']
print(sheet.title)

#Guardar cambios en el archivo excel
excel_document.save(libro)

#se crea un cursor
cursor = conexion.cursor()

selectEstadoCivil = "SELECT cCodigoEstadoCivil, cDescripcionEstadoCivil FROM EstadoCivil"

cursor.execute(selectEstadoCivil)

rows = cursor.fetchall()

#print(rows)

#for row in rows:
#excel_document['DanielEstadoCivil'].active
hojaDanielEstadoCivil = excel_document.active
#print(hojaDanielEstadoCivil)

#Titulo de las columnas
hojaDanielEstadoCivil["A1"] = "Codigo"
hojaDanielEstadoCivil["B1"] = "Descripcion"

#Letras de las columnas
celdaB="B"
celdaA="A"

#Contador para aumentar las filas dentro del excel
n=1
for row in rows:
    #se aumenta el contador para que se realicen los cambios en cada celda de manera descendente
    n+=1
    #En esta variable se guardan los registros de la BD en la columna cDescripcionEstadoCivil
    descripcion = row.cDescripcionEstadoCivil
    #En esta variable se guardan los registros de la BD en la columna cCodigoEstadoCivil
    codigo = row.cCodigoEstadoCivil

    #Se añaden los registros en las celdas correspondientes del excel
    hojaDanielEstadoCivil[f'{celdaA}{n}'] = codigo
    hojaDanielEstadoCivil[f'{celdaB}{n}'] = descripcion
    
#Se guarda el documento para que se apliquen los cambios
excel_document.save(libro)