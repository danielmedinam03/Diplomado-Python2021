import pyodbc 
#ESTA LINEA ES PARA VERIFICAR LOS CONTROLADORES QUE HAY INSTALADOS
#[x for x in pyodbc.drivers() if x.startswith("Microsoft Access Driver")]

# Cadena de conexion al servidor 
cadena = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'r'DBQ=C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases_de_Datos_Access\Database1.accdb;')

#CONEXION CON LA BD
conexion= pyodbc.connect(cadena)
"""
# SELECCIONA DATOS DE LA TABLA "GENERO" ORDENADA MEDIANTE EL CODIGO DEL GENERO
cGeneroSelect= "SELECT cDescripcionGenero,cCodigoGenero FROM Genero ORDER BY cCodigoGenero"

#SE CREA UN CURSOR
Genero = conexion.cursor()

#EL EXECUTE LO QUE HACE ES ASIGNARLE A EL CURSOR UNA VARIABLE PARA QUE ALMACENE LO QUE HAY AHI
Genero.execute(cGeneroSelect)

#SE CREA UNA VARIABLE ROWS, QUE ALMACENA TODOS (FECTHALL) LOS CAMPOS DE LA TABLA
rows = Genero.fetchall()
#print(rows)

if rows is not None:
    for row in rows:
        print(row)
        
else: 
    print("PEDORRO No hay datos en la tabla genero")
"""
# INSERTA REGISTROS EN LA TABLA GENERO CON LOS VALORES ASIGNADOS
cGeneroInsert = "INSERT INTO Genero(cCodigoGenero, cDescripcionGenero) VALUES ('F','Masculino')"

# SE CREA EL CURSOR
Genero = conexion.cursor()
# AL CURSOR SE LE PASA POR PARAMETRO EL VALOR DE LA CADENA INSERT DEL GENERO
Genero.execute(cGeneroInsert)

# SE REALIZA UN COMMIT PARA GUARDAR
Genero.commit()

Genero.close()
conexion.close()

