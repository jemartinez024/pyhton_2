def display_seven_segment(number):
    digits = [
        ["###",
         "# #",
         "# #",
         "# #",
         "###"],  # 0

        ["  #",
         "  #",
         "  #",
         "  #",
         "  #"],  # 1

        ["###",
         "  #",
         "###",
         "#  ",
         "###"],  # 2

        ["###",
         "  #",
         "###",
         "  #",
         "###"],  # 3

        ["# #",
         "# #",
         "###",
         "  #",
         "  #"],  # 4

        ["###",
         "#  ",
         "###",
         "  #",
         "###"],  # 5

        ["###",
         "#  ",
         "###",
         "# #",
         "###"],  # 6

        ["###",
         "  #",
         "  #",
         "  #",
         "  #"],  # 7

        ["###",
         "# #",
         "###",
         "# #",
         "###"],  # 8

        ["###",
         "# #",
         "###",
         "  #",
         "###"],  # 9
    ]
    
    # Convertimos el número a una cadena
    num_str = str(number)
    
    # Iteramos por las 5 filas
    for row in range(5):
        line = ""
        for digit in num_str:
            line += digits[int(digit)][row] + " "
        print(line.rstrip())  # Eliminamos el espacio al final

# Prueba con entrada del usuario
user_input = input("Introduce un número: ")
if user_input.isdigit():
    display_seven_segment(user_input)
else:
    print("Por favor, introduce solo números enteros no negativos.")
