def calcular_descuento(precio, descuento=10):
    """Cälculo del descuento al monto total de una compra.
    :param precio: Monto total de la compra.
    :param descuento: Porcentaje de descuento (10% por defecto).
    :return: Monto del descuento
    """
    # Caculamos el monto del descuento
    monto_descuento = precio * descuento / 100

    # Redondeamos el resultado a 2 decimales
    return round(monto_descuento, 2)


# Llamadas a la función con diferentes argumentos
monto1 = 205.25
descuento1 = calcular_descuento(monto1)  # Usamos el descuento por defecto
monto_final1 = monto1 - descuento1  # Precio final después del descuento

monto2 = 205.25
descuento2 = calcular_descuento(monto2, 15)  # Usamos un 15% de descuento.
monto_final2 = monto2 - descuento2

# Mostramos los resultados en pantalla
print("=" * 70)

print(f"Compra 1: Monto total: ${monto1}, Descuento: ${descuento1}, Monto final: {monto_final1:.2f}")
print(f"Compra 2: Monto total: ${monto2}, Descuento: ${descuento2}, Monto final: ${monto_final2:.2f}")

print("=" * 70)