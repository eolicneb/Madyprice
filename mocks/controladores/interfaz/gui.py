import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, TypeVar, Generic
from modelos.controladores.presupuesto import ControladorDeInterfaz, ControladorDePresupuesto

T = TypeVar('T')


class ModelCombobox(ttk.Combobox, Generic[T]):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self._objects: List[T] = []
        self._string_var = tk.StringVar()
        self.configure(textvariable=self._string_var)
        self._string_var.trace_add('write', self._on_select)

    def set_objects(self, objects: List[T]):
        self.set('')
        self._objects = objects
        self['values'] = [str(obj) for obj in objects]

    def get_selected_object(self) -> T:
        current_index = self.current()
        if current_index != -1:
            return self._objects[current_index]
        return None

    def _on_select(self, *args):
        # Este método se llama cuando cambia la selección
        pass

    def set_selected_object(self, obj: T):
        if obj in self._objects:
            index = self._objects.index(obj)
            self.current(index)


class InterfazTkinter(tk.Tk, ControladorDeInterfaz):
    def __init__(self):
        self._controlador = None
        super().__init__()
        self.title("Sistema de Presupuestos")
        self.geometry("700x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.frame_nuevo = ttk.Frame(self.notebook)
        self.frame_mostrar = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_nuevo, text="Nuevo Presupuesto")
        self.notebook.add(self.frame_mostrar, text="Mostrar Presupuesto")

        self.lista_de_clientes = None
        self.lista_de_vendedores = None
        self.lista_de_formatos = None
        self.lista_de_items = None

        self.setup_nuevo_presupuesto()
        self.setup_mostrar_presupuesto()

    @property
    def controlador(self):
        return self._controlador

    @controlador.setter
    def controlador(self, nuevo_controlador: ControladorDePresupuesto):
        self._controlador = nuevo_controlador
        if self._controlador:
            self.actualizar_combos()

    def setup_nuevo_presupuesto(self):
        ttk.Button(self.frame_nuevo, text="Guardar Presupuesto", command=self.nuevo_presupuesto).pack(pady=10)

        self.cliente_var = tk.StringVar()
        self.vendedor_var = tk.StringVar()
        # self.formato_var = tk.StringVar()

        ttk.Label(self.frame_nuevo, text="Cliente:").pack()
        self.cliente_combo = ModelCombobox(self.frame_nuevo, textvariable=self.cliente_var)
        self.cliente_combo.pack()

        ttk.Label(self.frame_nuevo, text="Vendedor:").pack()
        self.vendedor_combo = ModelCombobox(self.frame_nuevo, textvariable=self.vendedor_var)
        self.vendedor_combo.pack()

        # ttk.Label(self.frame_nuevo, text="Formato:").pack()
        # self.formato_combo = ModelCombobox(self.frame_nuevo, textvariable=self.formato_var)
        # self.formato_combo.pack()

        ttk.Button(self.frame_nuevo, text="Agregar Items", command=self.agregar_items).pack(pady=10)

        self.items_listbox = tk.Listbox(self.frame_nuevo, width=50)
        self.items_listbox.pack(pady=10)

        self.items = []
        self.item_objects = []

    def setup_mostrar_presupuesto(self):
        self.presupuesto_text = tk.Text(self.frame_mostrar, height=20, width=50)
        self.presupuesto_text.pack(pady=10)
        self.actualizar_combos()

    def nuevo_presupuesto(self):
        self.controlador.nuevo_presupuesto()
        self.actualizar_combos()
        self.items_listbox.delete(0, tk.END)
        messagebox.showinfo("Nuevo Presupuesto", "Se ha creado un nuevo presupuesto")

    def actualizar_combos(self):
        if self.controlador is not None:
            self.cliente_combo.set_objects(self.controlador.lista_de_clientes())
            self.vendedor_combo.set_objects(self.controlador.lista_de_vendedores())
            # self.formato_combo.set_objects(self.controlador.lista_de_formatos())
            self.item_objects = self.controlador.lista_de_items()
        else:
            self.cliente_combo.set_objects([])
            self.vendedor_combo.set_objects([])
            # self.formato_combo.set_objects([])
            self.item_objects = []

    def agregar_items(self):
        self.item_objects = self.controlador.lista_de_items()
        items_str = [str(item) for item in self.item_objects]
        item = tk.StringVar()
        dialog = tk.Toplevel(self)
        dialog.title("Agregar Item")
        ttk.Label(dialog, text="Seleccione un item:").pack()
        item_combo = ttk.Combobox(dialog, textvariable=item, values=items_str)
        item_combo.pack()
        ttk.Button(dialog, text="Agregar",
                   command=lambda: self.agregar_item(item.get(), item_combo.current(), dialog)).pack()

    def agregar_item(self, item, item_id, dialog):
        if item:
            self.items_listbox.insert(tk.END, item)
        if item_id != -1:
            self.items.append(self.item_objects[item_id])
        dialog.destroy()

    def mostrar_presupuesto(self, presupuesto):
        self.notebook.select(self.frame_mostrar)
        self.presupuesto_text.delete('1.0', tk.END)
        self.presupuesto_text.insert(tk.END, f"PRESUPUESTO:\n")
        self.presupuesto_text.insert(tk.END, f"Cliente: {presupuesto.cliente}\n")
        self.presupuesto_text.insert(tk.END, f"Vendedor: {presupuesto.vendedor}\n")
        self.presupuesto_text.insert(tk.END, f"Items:\n")
        for i, item in enumerate(presupuesto.items):
            self.presupuesto_text.insert(tk.END, f"[{i}] {item}\n")
        self.presupuesto_text.insert(tk.END, "-" * 30 + "\n")
        self.presupuesto_text.insert(tk.END, f"TOTAL: $ {presupuesto.total:.2f}\n")

    def mostrar_error_de_presupuesto(self, error):
        messagebox.showerror("Error de Presupuesto", str(error))

    def pedir_cliente(self):
        return self.cliente_combo.get_selected_object()

    def pedir_vendedor(self):
        return self.vendedor_combo.get_selected_object()

    def pedir_formato(self):
        return self.formato_combo.get_selected_object()

    def pedir_items(self):
        return self.items


if __name__ == "__main__":
    app = InterfazTkinter()
    app.mainloop()
