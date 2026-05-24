class Inventario:

    #Constructor por defecto que contiene un atributo llamado “objetos”
    #instanciado a un diccionario vacío
    def __init__(self):
        self.objetos = {}

    #Método “añadir_objeto” que recibe por parámetro un nombre y una
    #cantidad. Debes comprobar si existe dicho nombre en el diccionario, si
    #es así entonces solo añades la cantidad, si no, añades una nueva
    #entrada en el diccionario con el nombre y la cantidad
    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad

    #Método “usar_objeto” que recibe por parámetro el objeto a usar. Lo
    #único que hace es disminuir la cantidad de dicho objeto. Debes tener
    #en cuenta que si la cantidad cae a 0, el objeto debe desaparecer del
    #inventario.
    def usar_objeto(self, objeto):
        if objeto in self.objetos:
            self.objetos[objeto] -= 1
            if self.objetos[objeto] == 0:
                self.objetos.pop(objeto)