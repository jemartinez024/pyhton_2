date = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")


#int_num = int(date)

adding = 0

for char in date:
    number = int(char)
    adding += number

print(adding)

number_add = 0

while adding >= 10:
    num_str = str(adding) # Convertir numero a cadena 
    temp_sum = 0
    for digit_char in num_str:
        temp_sum += int(digit_char)
    adding = temp_sum
    
print("Tu Dígito de la Vida es:", adding)

    
        