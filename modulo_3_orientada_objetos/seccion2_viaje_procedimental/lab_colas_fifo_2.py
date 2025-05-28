"""Tu tarea es extender ligeramente las capacidades de la clase Queue. Queremos que tenga un método sin parámetros que devuelva True si la cola está vacía y False de lo contrario.

Completa el código que te proporcionamos en el editor. Ejecútalo para comprobar si genera un resultado similar al nuestro.

A continuación, puedes copiar el código que usamos en el laboratorio anterior"""

class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []#
        # Escribe el código aquí.
        #

    def put(self, elem):
        self.queue.insert(0, elem)
        # Escribe el código aquí.
        #

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def isempty(self):
        return len(self.queue) ==0
    
    # Escribe código nuevo aquí.
    #


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")