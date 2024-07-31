from modelos.controladores.presupuesto import ControladorDeInterfaz


class Interfaz(ControladorDeInterfaz):
    def __init__(self, controlador=None):
        self.controlador = controlador

    def nuevo_presupuesto(self):
        self.controlador.nuevo_presupuesto()

    def pedir_cliente(self):
        print("ELIJA UN CLIENTE:")
        tabla = self.controlador.lista_de_clientes()
        for i, cliente in enumerate(tabla):
            print(f"[{i}] {cliente}")
        cliente_id = int(input("ID de cliente: "))
        return tabla[cliente_id]

    def pedir_vendedor(self):
        print("ELIJA UN VENDEDOR:")
        tabla = self.controlador.lista_de_vendedores()
        for i, vendedor in enumerate(tabla):
            print(f"[{i}] {vendedor}")
        vendedor_id = int(input("ID de vendedor: "))
        return tabla[vendedor_id]

    def pedir_formato(self):
        print("ELIJA UN FORMATO:")
        tabla = self.controlador.lista_de_formatos()
        for i, formato in enumerate(tabla):
            print(f"[{i}] {formato}")
        formato_id = int(input("ID de formato: "))
        return tabla[formato_id]

    def pedir_item(self):
        print("ELIJA UN ITEM:")
        tabla = self.controlador.lista_de_items()
        for i, item in enumerate(tabla):
            print(f"[{i}] {item}")
        item_id = int(input("ID de item: "))
        return tabla[item_id]

    def pedir_items(self):
        def consultar_agregar():
            agregar = 'x'
            while agregar not in 'snSN':
                agregar = input("AGREGAR ITEM? [s/n] ")
            return agregar.lower()

        items = []
        agregar = consultar_agregar()
        while agregar == "s":
            items.append(self.pedir_item())
            agregar = consultar_agregar()
        return items

    def mostrar_presupuesto(self, presupuesto):
        print("PRESUPUESTO:")
        print(f"Cliente: {presupuesto.cliente}")
        print(f"Vendedor: {presupuesto.vendedor}")
        print(f"Items:")
        for i, item in enumerate(presupuesto.items):
            print(f"[{i}] {item}")
        print("-"*40)
        print(f"TOTAL: $ {presupuesto.total:.2f}")

    def mostrar_error_de_presupuesto(self, error):
        print("ERROR DE PRESUPUESTO")
        print(str(error))
        print("!!!")
