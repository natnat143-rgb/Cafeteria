import tkinter as tk
from tkinter import messagebox

"""
Esta aplicación utiliza Tkinter para crear una interfaz gráfica.
La app tendrá 5 pantallas:

1. Pantalla de inicio
2. Menú (selección de platillos y bebidas)
3. Confirmación del pedido
4. Ticket final
5. Mensaje de agradecimiento
"""


class App:
    def _init_(self, root):
        # Ventana principal
        self.root = root
        self.root.title("Aplicación de Menú")
        self.root.geometry("450x550")

        # VARIABLES QUE GUARDARÁN LA SELECCIÓN DEL USUARIO

        # Diccionario que guardará si cada platillo está seleccionado o no
        self.platillos_vars = {}

        # Guardará la bebida seleccionada (solo una)
        self.bebida_seleccionada = tk.StringVar()

        # Guardará el método de pago elegido
        self.metodo_pago = tk.StringVar()

        # Llamamos a la primera pantalla
        self.pantalla_inicio()


    # --------------------------------------------------
    # 1. PANTALLA DE INICIO
    # --------------------------------------------------
    def pantalla_inicio(self):
        self.limpiar_ventana()

        # Título principal
        tk.Label(self.root, text="Bienvenido a Mi Restaurante",
                 font=("Arial", 20)).pack(pady=60)

        # Botón para ir al menú
        tk.Button(
            self.root,
            text="Entrar al menú",
            font=("Arial", 16),
            command=self.pantalla_menu
        ).pack()


    # --------------------------------------------------
    # 2. PANTALLA DE MENÚ
    # --------------------------------------------------
    def pantalla_menu(self):
        self.limpiar_ventana()

        # Título
        tk.Label(self.root, text="Selecciona tus platillos",
                 font=("Arial", 18)).pack(pady=10)

        # Lista de platillos disponibles
        platillos = ["Hamburguesa", "Pizza", "Tacos", "Boneless", "Papas"]
        self.platillos_vars = {}  # Reiniciar diccionario por si el usuario regresa

        # Se crean Checkbuttons para que el usuario pueda elegir varios platillos
        for p in platillos:
            var = tk.BooleanVar()  # Variable booleana (True/False)
            self.platillos_vars[p] = var

            tk.Checkbutton(
                self.root,
                text=p,
                variable=var,   # variable asociada al check
                font=("Arial", 14)
            ).pack(anchor="w", padx=20)

        # Sección de bebidas
        tk.Label(self.root, text="Elige una bebida:",
                 font=("Arial", 18)).pack(pady=10)

        bebidas = ["Coca-Cola", "Sprite", "Agua", "Jugo"]

        # Radiobuttons: solo se puede elegir 1 bebida
        for b in bebidas:
            tk.Radiobutton(
                self.root,
                text=b,
                variable=self.bebida_seleccionada,
                value=b,
                font=("Arial", 14)
            ).pack(anchor="w", padx=20)

        # Botón para continuar a la confirmación
        tk.Button(
            self.root,
            text="Continuar",
            font=("Arial", 16),
            command=self.pantalla_confirmacion
        ).pack(pady=20)


    # --------------------------------------------------
    # 3. PANTALLA DE CONFIRMACIÓN DEL PEDIDO
    # --------------------------------------------------
    def pantalla_confirmacion(self):
        # Obtener lista de platillos seleccionados
        platillos_seleccionados = [p for p, v in self.platillos_vars.items() if v.get()]

        # Validar que se haya elegido al menos un platillo
        if not platillos_seleccionados:
            messagebox.showwarning("Error", "Debes seleccionar al menos un platillo.")
            return

        # Validar que haya bebida seleccionada
        if self.bebida_seleccionada.get() == "":
            messagebox.showwarning("Error", "Debes elegir una bebida.")
            return

        self.limpiar_ventana()

        # Título
        tk.Label(self.root, text="Confirmación del Pedido",
                 font=("Arial", 20)).pack(pady=20)

        # Mostrar platillos seleccionados
        tk.Label(self.root, text="Platillos elegidos:",
                 font=("Arial", 16)).pack()

        for p in platillos_seleccionados:
            tk.Label(self.root, text=f"• {p}", font=("Arial", 14)).pack()

        # Mostrar bebida elegida
        tk.Label(
            self.root,
            text=f"Bebida: {self.bebida_seleccionada.get()}",
            font=("Arial", 16),
            pady=10
        ).pack()

        # Métodos de pago disponibles
        tk.Label(self.root, text="Método de pago:",
                 font=("Arial", 18)).pack(pady=10)

        # Radiobuttons: solo un método de pago se puede elegir
        metodos = ["Tarjeta", "Efectivo", "Transferencia"]
        for m in metodos:
            tk.Radiobutton(
                self.root,
                text=m,
                variable=self.metodo_pago,
                value=m,
                font=("Arial", 14)
            ).pack(anchor="w", padx=20)

        # Botón para generar ticket
        tk.Button(
            self.root,
            text="Generar Ticket",
            font=("Arial", 16),
            command=self.pantalla_ticket
        ).pack(pady=20)


    # --------------------------------------------------
    # 4. PANTALLA DEL TICKET FINAL
    # --------------------------------------------------
    def pantalla_ticket(self):
        # Validar método de pago
        if self.metodo_pago.get() == "":
            messagebox.showwarning("Error", "Debes elegir un método de pago.")
            return

        self.limpiar_ventana()

        # Título
        tk.Label(self.root, text="Ticket de Compra",
                 font=("Arial", 20)).pack(pady=20)

        # Obtener platillos seleccionados
        platillos = [p for p, v in self.platillos_vars.items() if v.get()]

        # Crear el texto del ticket
        texto_ticket = "Restaurante XYZ\n-----------------------\n"
        texto_ticket += "Platillos:\n"

        for p in platillos:
            texto_ticket += f" - {p}\n"

        texto_ticket += f"\nBebida: {self.bebida_seleccionada.get()}\n"
        texto_ticket += f"Pago con: {self.metodo_pago.get()}\n"
        texto_ticket += "-----------------------\n"
        texto_ticket += "¡Gracias por tu compra!\n"

        # Mostrar el ticket
        tk.Label(
            self.root,
            text=texto_ticket,
            font=("Consolas", 12),
            justify="left"
        ).pack(pady=10)

        # Botón de finalización
        tk.Button(
            self.root,
            text="Finalizar",
            font=("Arial", 16),
            command=self.pantalla_gracias
        ).pack(pady=20)


    # --------------------------------------------------
    # 5. PANTALLA FINAL DE AGRADECIMIENTO
    # --------------------------------------------------
    def pantalla_gracias(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="¡Gracias por tu compra!",
                 font=("Arial", 22)).pack(pady=60)

        tk.Label(self.root, text="Esperamos verte pronto 😊",
                 font=("Arial", 16)).pack()


    # --------------------------------------------------
    # FUNCIÓN QUE LIMPIA TODA LA VENTANA ACTUAL
    # --------------------------------------------------
    def limpiar_ventana(self):
        # Borra todos los widgets de la pantalla
        for widget in self.root.winfo_children():
            widget.destroy()


# --------------------------------------------------
# EJECUCIÓN DE LA APLICACIÓN
# --------------------------------------------------
root = tk.Tk()
app = App(root)
root.mainloop()