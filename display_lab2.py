digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Ingresa el número que deseas mostrar: ")))
    

"""🧠 ¿Qué estamos haciendo?
Estamos imprimiendo un número como si estuviera en un display de siete segmentos, línea por línea. Cada número está representado por 5 líneas, así que tenemos que imprimir 5 filas en total.

🔍 Línea por línea
1. for row in range(5):
Estamos diciendo: "vamos a imprimir 5 filas" (de arriba a abajo).

Cada row vale: 0, 1, 2, 3, 4.

Estas filas representan:

0: parte superior del dígito

1: parte superior intermedia

2: centro

3: parte inferior intermedia

4: parte inferior

2. line = ""
Creamos una cadena vacía llamada line.

Aquí vamos a ir agregando las representaciones de cada dígito para la fila actual (row).

3. for digit in num_str:
Recorremos cada dígito que el usuario escribió.

Por ejemplo, si el usuario escribe "123", entonces este for hará:

digit = '1'

digit = '2'

digit = '3'

4. line += digits[int(digit)][row] + " "
Convertimos el carácter digit a entero para poder acceder al patrón en la lista digits.

Por ejemplo, int('2') = 2, y digits[2] es la lista de las 5 líneas para el número 2.

Luego accedemos a la fila específica de ese dígito con [row].

Le agregamos un espacio " " al final para que los números no se peguen.

Ejemplo (cuando row = 0 y num_str = "123"):

digits[1][0] = " #"

digits[2][0] = "###"

digits[3][0] = "###"

Resultado: line = " # ### ### "

5. print(line.rstrip())
Imprimimos la línea resultante sin el espacio extra al final (rstrip() quita los espacios a la derecha).

Luego se pasa a la siguiente fila (row = 1, row = 2, etc.)

✅ Resultado final:
Si el usuario ingresa 123, el ciclo imprime:


  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

Cada línea es una fila del display, construida horizontalmente dígito por dígito.

"""