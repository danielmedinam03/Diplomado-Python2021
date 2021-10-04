import pyodbc 

[x for x in pyodbc.drivers() if x.startswith("Microsoft Access Driver")]

cadena = (r'DRIVER=(Microsoft Access Driver(*.mdb, *accdb))};'r'DBQ=C:\Users\PC\Documents\Daniel\RETOVIBRA\Python\Bases de Datos Access\Database1.accdb')
conexion= pyodbc.connect(cadena)

