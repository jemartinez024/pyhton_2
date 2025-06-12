"""4.1.5 La función lambda
La función lambda es un concepto tomado de las matemáticas, más específicamente, de una parte llamada el Cálculo Lambda, pero estos dos fenómenos no son iguales.

Los matemáticos usan el Cálculo Lambda en sistemas formales conectados con: la lógica, la recursividad o la demostrabilidad de teoremas. Los programadores usan la función lambda para simplificar el código, hacerlo más claro y fácil de entender.

Una función lambda es una función sin nombre (también puedes llamarla una función anónima). Por supuesto, tal afirmación plantea inmediatamente la pregunta: ¿cómo se usa algo que no se puede identificar?

Afortunadamente, no es un problema, ya que se puede mandar llamar dicha función si realmente se necesita, pero, en muchos casos la función lambda puede existir y funcionar mientras permanece completamente de incógnito.

La declaración de la función lambda no se parece a una declaración de función normal; compruébalo tu mismo:

lambda parameters: expression"""


two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

