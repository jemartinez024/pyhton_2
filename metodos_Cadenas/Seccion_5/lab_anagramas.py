print("*** Bienvendo al comprobador de Anagramas ***")

# Ingresa el texto.
text1 = input("Ingresa la pirmera palabra: ")
text2 = input("Ingresa la segunda palabra: ")

text1 = text1.replace(' ','')  ## Elimina los espacios en blanco que pueda tener
text2 = text2.replace(' ','')  ## Elimina los espacios en blanco que pueda tener

text1 = text1.upper() # Convierte a mayusculas.
text2 = text2.upper() # Convierte a mayusculas.


char_list1 = list(text1) # Convierte cadenas en listas
char_list2 = list(text2)

orden1 = sorted(char_list1) # Ordena las listas
orden2 = sorted(char_list2)

string_add1 = "".join(orden1) # Une los elementos de cada lista en cadenas separadas
string_add2 = "".join(orden2)



#print(string_add1 + string_add2)

if string_add1 == string_add2:
    print('Son anagramas')
else:
    print('No Son anagramas')