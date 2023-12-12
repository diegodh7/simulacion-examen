#Pedido. clase, entidad
#atributos, campos, propiedades : id,fechaPedido,idcliente,idproducto,unidades
#métodos: comprar, devolver,facturarPDF, enviarSMS
from Cliente import Cliente #utilizar clase Cliente de mi proyecto
from Producto import Producto


#nomenclatura : mayúsculas, minúsculas, espacios,
#camelCase : funciones, métodos
#snake_case : variables
#PascalCase : clases

class Pedido:
    def __init__(self,id,fecha_pedido,id_cliente,id_producto,unidades):
        self.id=id
        self.fecha_pedido=fecha_pedido
        self.id_cliente=id_cliente
        self.id_producto=id_producto
        self.unidades=unidades

    def comprar(self):
        print('el cliente compra')
    def enviarSMS(self):
        print('envio sms')
    def facturar(self):
        print(f'Factura {self.id}')
        print(f'Nombre de cliente {self.id_cliente}')
        print(f'Unidades compradas {self.unidades}')

#crear un pedido
pedido1=Pedido('A1','10/05/2022',1,1,5) #no tiene en cuenta el cliente ni el producto
#tabla sin relaciones
pedido1.facturar()
#crear otro pedido
cliente100=Cliente(100,'maria','sevilla',True)
producto20=Producto(20,'sombrero',15,9.95,'05/10/2022')
pedido2=Pedido('A2','11/05/2022',cliente100,producto20,7)#tabla relacionada
#fijate que puedes pasar como idcliente un objeto porque idcliente en pedidos es Any
pedido2.facturar()

#no hemos hecho
#herencia
#polimorfismo (no entra)
#encapsulamiento (no entra)
#sobrecarga
#sobreescritura
