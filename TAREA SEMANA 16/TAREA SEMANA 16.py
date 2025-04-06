# Escritura de archivo de texto
# Abrimos el archivo en modo escritura ("w")
archivo = open("my_notes.txt", "w")

# Usamos el método write() para escribir tres líneas
archivo.write(" Hoy fue la ultima clase de fundamentos de programacion\n")
archivo.write("Esperamos que el proximo semestre nos vuelva a dar clases ud.\n")
archivo.write("Hasta la próxima clase, gracias.\n")

# Cerramos el archivo después de escribir
archivo.close()
# Abrimos el archivo en modo lectura ("r")
archivo = open("my_notes.txt", "r")

print("Contenido del archivo línea por línea:")

# Usamos readline() para leer una línea a la vez
linea = archivo.readline()
while linea:
    print(linea.strip())  # strip() para quitar el salto de línea al final
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
