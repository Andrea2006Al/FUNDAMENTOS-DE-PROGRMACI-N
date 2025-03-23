#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
informacion_personal = {"nombre": "Juan", "edad": 25, "ciudad": "lago agrio"}
print(informacion_personal)
#Acceder
print(informacion_personal["ciudad"])
 #Modificar
informacion_personal["ciudad"]="El coca"
print(informacion_personal)
#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
informacion_personal["profesion"]="programador"
print(informacion_personal)
#Verificar Existencia de Claves:
#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if"telefono" in informacion_personal:
    print("la clave telefono existe")
else:
    print("la clave telefono no existe")
#Si no existe, agrégala con un número de teléfono ficticio.
informacion_personal["telefono"]= " 0993584816"
print(informacion_personal)
#Eliminar una Clave:
#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal["edad"]
print(informacion_personal)

