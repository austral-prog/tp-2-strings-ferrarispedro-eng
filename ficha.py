def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre=input("Ingrese su nombre completo: ").strip().lower()
    email=input("Ingrese su Email: ")
    nota_1=int(input("Nota 1 = "))
    nota_2=int(input("Nota 2 = "))
    nota_3=int(input("Nota 3 = "))

    print(f"{'='*24}")
    print(f"    Ficha del alumno".upper())
    print(f"{'='*24}")
    print(f"Nombre: {(nombre.strip()).title()}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre)}")
    iniciales=int(nombre.find(" ")+1)
    print(f"Iniciales: {nombre[0].upper()}{nombre[iniciales].upper()}")
    ubicacion_apellido=nombre.find(" ")+1
    print(f"Usuario: {nombre[ubicacion_apellido::].lower()}.{(nombre[:ubicacion_apellido]).lower()}".rstrip())
    print(f"Email valido: {'@' in email}")
    dominio_email=(email.find('@')+1)
    print(f"Dominio: {email[dominio_email::].lower()}")
    print(f"Nombre para archivo: {nombre.replace(" ", "_").title()}")
    print(f"Cantidad de a: {nombre.count('a')}")
    print(f"Codigo secreto: {nombre[-1::-1].upper()}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {(nota_1+nota_2+nota_3)}")
    print(f"Promedio: {(nota_1+nota_2+nota_3)/3}")
    print(f"Promedio entero: {(nota_1 + nota_2 + nota_3) // 3}")
    print(f"{'='*24}")

#ficha()