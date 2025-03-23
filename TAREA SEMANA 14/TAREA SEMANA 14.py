#Crea una función llamada calcular_descuento que tome dos parámetros:
# el monto total de la compra y un valor predeterminado para el porcentaje de descuento
# (por ejemplo, 10% por defecto).
def descuento(monto_total, valor_descuento=35):
    resp = monto_total * (valor_descuento / 100)
    total = Subtotal - resp
    return resp,total
#llamar  a la funcion
#Llamar el subtotal
Subtotal= 4500
resp = descuento(4500)
print(f"subtotal: {Subtotal}")
print(f"Descuento: {resp}")
print(f"total a pagar: {resp[1]}")



