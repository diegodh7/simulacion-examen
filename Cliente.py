#POO : patrón de desarrollo. Clase - objeto
#empresa : CRM : customer relational manager
#cliente : objeto. clase (plantilla)
#propiedades:codigo, nif, nombre, email, ciudad,activo, descuento...
#métodos: añadir carrito, add lista de deseos, compra, pago, pago aplazado, seguimiento compra, devolucion, recomendar compras..
#producto : objeto. clase (plantilla)
#propiedades : codigo, nombre, familia, precio, unitstock, descuento, fecha caducidad, externo,
#metodos: pedirnuevostock, devolverproductodevuelto
#proveedor. clase. objeto
#pedidos : clase, objeto.
#propieddaes: fecha fra, numero fra, cliente, producto, fecha entrega, trnasportistas, recoge pedido, dirección envío
#metodos : firmarentrega
#Crer una clase, entidad, modelo, dataClass
class Cliente:#clase, entidad
    #propiedades / atributos / campos / adjetivos calificativos
    def __init__(self,id,nombre,ciudad,prime): #constructor
        self.id=id
        self.nombre=nombre
        self.ciudad=ciudad
        self.prime=prime
    def comprar(self): #método de instancia
        print('cliente compra') #implementar el método
    def valorar(self):
        print('cliente valora la compra')
    def consultarFicha(self):
        print(f'Nombre: {self.nombre}, ciudad: {self.ciudad} Eres Prime? {self.prime}')
    def fichaPDF(self):
        print(f'Cliente {self.nombre} en PDF')
#usar la clase
cliente1=Cliente(1,'juan','madrid',True) #alta un cliente. instanciar la clase
print(cliente1.nombre)
cliente1.consultarFicha()
cliente1.fichaPDF()