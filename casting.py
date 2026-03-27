def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio=int(input("Ingrese el precio: "))
    descuento=float(input("Ingrese el descuento: "))
    cantidad=int(input("Ingrese una cantidad: "))
    precio_descuento=(precio-descuento)
    precio_total=(precio_descuento*cantidad)

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_descuento}")
    print(f"Total: {precio_total}")


#casting()