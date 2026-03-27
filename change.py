def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("Ingresar gasto: "))

    dinero_recibido = int(input("Ingresa el dinero recibido: "))

    print("Ingresar gasto:"
          "")
    print(gasto)

    print("Dinero recibido"
          "")
    print(dinero_recibido)

    print("")

    print("Vuelto")

    print("")
    print("Pesos:")

    vuelto = dinero_recibido - gasto

    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print(pesos)
    print("Centavos:")
    print(centavos)

#change()
