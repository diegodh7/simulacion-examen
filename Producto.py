#POO
#entidad : Producto. clase.
#propiedades, campos, atributos : id,nombre,unidades,precio,fechaFabricacion
#metodos:reponerStock, aplicarDescuento

class Producto: #clase, entidad, modelo
    def __init__(self,id,nombre,unidades,precio,fechaFabricacion): #constructor
        self.id=id #almacenar en la instancia el parámetro
        self.nombre=nombre #string
        self.unidades=unidades #entero
        self.precio=precio #con decimales
        self.fechaFabricacion=fechaFabricacion #fecha
        #Python utiliza inferencia de tipos. Por eso NO es necesario
        #indicar el tipo de dato al declarar la variable
        #si Python NO tiene todavía el dato, por defecto el tipo es Any

        #explicar en memoria qué diferencia hay entre tipado fuerte, débil y inferencia de tipado
        #compilados habitualmente son tipado fuerte.
        #interpretados suelen usar tipado por inferencia o a veces, tipado débil
    def reponerStock(self):
        if self.unidades<10:
            print('tenemos que pedir unidades para evitar rotura de stock')
        else:
            print(f'mi Stock actual es {self.unidades}')

producto1=Producto(100,'camisa',50,9.95,'10/05/2022')
producto2=Producto(200,'pantalón',9,24.95,'10/05/2022')
producto1.reponerStock()
producto2.reponerStock()
