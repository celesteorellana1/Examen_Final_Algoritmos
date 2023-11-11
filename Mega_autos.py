#Crear un programa que tenga la capacidad de escribir datos de archivos Excel
import openpyxl

#cargamos el documento excel
libro = openpyxl.load_workbook("vehiculos.xlsx")

#abrimos la hoja llamada 'listado'
hoja = libro['listado']

#Crear encabezados 
hoja['A1'].value = "codigo"
hoja['B1'].value = "marca"
hoja['C1'].value = "modelo"
hoja['D1'].value = "precio"
hoja['E1'].value = "Kilometraje"

#nos posicionamos en la fila 2 del excel
proxima_fila = hoja.max_row + 1

#Funcion para guardar un archivo un vehiculo en el archivo de Excel
def guardar_vehiculos():
    #Obtener los valores ingresados en los campos de entrada
    codigo = codigo.entry.get(),
    marca = marca.entry.get(),
    modelo = modelo.entry.get()
    precio = float(precio.entry.get())
    kilometraje = int(kilometraje.entry.get())

#Funcion para eliminar un vehiculo del archivo de excel
def eliminar_vehiculo():
    #obtener el codigo del vehiculo a eliminar
    codigo = codigo.entry.get()

#guardar el archivo
libro.save("vehiculos.xlsx")
