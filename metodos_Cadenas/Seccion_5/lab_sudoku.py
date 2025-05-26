# Una función que verifica si una lista contiene exactamente los dígitos del 1 al 9, sin repetir.
def checkset(digs):
    # Convierte la lista a una lista ordenada y la compara con ['1', '2', ..., '9']
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]

# Lista vacía donde se guardarán las 9 filas del Sudoku
rows = []

# Bucle para pedir las 9 filas al usuario
for r in range(9):
    ok = False  # Bandera para verificar que la fila ingresada sea válida
    while not ok:
        row = input("Ingresa fila #" + str(r + 1) + ": ")  # Solicita la fila
        # Verifica que tenga exactamente 9 caracteres y todos sean dígitos
        ok = len(row) == 9 and row.isdigit()
        if not ok:
            print("Datos de fila incorrectos: se requieren 9 dígitos (del 1 al 9)")
    rows.append(row)  # Guarda la fila en la lista

# Variable para indicar si el Sudoku es válido
ok = True

# Verifica cada fila
for r in range(9):
    if not checkset(rows[r]):
        ok = False  # Si una fila no contiene los dígitos correctos, el Sudoku no es válido
        break

# Verifica cada columna
if ok:
    for c in range(9):
        col = []  # Lista para la columna actual
        for r in range(9):
            col.append(rows[r][c])  # Agrega el dígito correspondiente de cada fila
        if not checkset(col):  # Verifica la columna
            ok = False
            break

# Verifica cada subcuadro de 3x3
if ok:
    for r in range(0, 9, 3):  # Recorre filas en saltos de 3 (0, 3, 6)
        for c in range(0, 9, 3):  # Recorre columnas en saltos de 3 (0, 3, 6)
            sqr = ''  # Cadena para almacenar los 9 dígitos del subcuadro
            for i in range(3):  # Recorre 3 filas del subcuadro
                sqr += rows[r + i][c:c + 3]  # Agrega 3 caracteres de cada fila
            if not checkset(list(sqr)):  # Verifica si los dígitos del subcuadro son válidos
                ok = False
                break

# Imprime el resultado final
if ok:
    print("Si")  # El Sudoku es válido
else:
    print("No")  # El Sudoku no es válido
