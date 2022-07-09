from asyncore import write
from cProfile import label
from doctest import master
from fileinput import filename
from tkinter import colorchooser, filedialog, font, messagebox, ttk
from tkinter import *
from turtle import undo



class Bloc(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master.title("Bloc de Notas")
        self.master.geometry("480x380")
        self.master.protocol("WM_DELETE_WINDOW", self.salir)
        self.n = 12
        self.f = "Arial"
        
        ttk.Button(self.master, text ="Abrir Fichero", command = self.crear_archivo).place(relx=0.90, rely=0.04)
        ttk.Button(self.master, text ="Crear Fichero", command = self.crear_archivo).place(relx=0.90, rely=0.04)
        ttk.Button(self.master, text ="Guardar Cambios", command = self.guardar_archivo).place(relx=0.90, rely=0.08)
        ttk.Button(self.master, text ="Cambiar Fondo", command = self.color_fondo ).place(relx=0.90, rely=0.12)
        ttk.Button(self.master, text ="Cambiar Fuente", command = self.fuente).place(relx=0.90, rely=0.16)
        ttk.Button(self.master, text ="Cambiar Color", command = self.color_texto).place(relx=0.90, rely=0.20)
        ttk.Button(self.master, text="Nueva Ventana", command = self.nueva_ventana).place(relx=0.90, rely=0.24)
        
        self.texto = Text(self.master, font = ("Arial", 12), undo = True, insertbackground = "red")
        self.texto.grid(column = 0, row = 1, sticky ="nsew")

    def señal(self):
        self.click = True

    
    def guardar_archivo(self):
        filename = filedialog.asksaveasfilename(defaultextension = ".txt")
        archivo = open(filename, "w")
        archivo.write(self.texto.get("1.0","end"))
        archivo.close()

    def fuente(self):
        self.tipo_de_fuente = Toplevel()
        self.tipo_de_fuente.overrideredirect(1)
        self.tipo_de_fuente.geometry("390x290")
        self.tipo_de_fuente.config(bg ="SeaGreen1", relief ="raised", bd = 3)
        self.tipo_de_fuente.bind("B1-Motion")
        self.tipo_de_fuente.bind("Presione-1")

        _fuente = list(font.families())
        tamañao = []
        for i in range(8,73):tamañao.append(i)

        Label(self.tipo_de_fuente, text = "Fuente:",fg = "black", bg = "SeaGreen1").grid(row = 0, column = 0, padx = 5, ipady= 6)
        Label(self.tipo_de_fuente, text = "Tamaño de Fuente:", fg = "black", bg = "SeaGreen1").grid(row = 0, column = 1, padx = 5, ipady = 6 )

        self.caja_fuente = ttk.Combobox(self.tipo_de_fuente, values = _fuente, justify = CENTER, width = 15, font = "Arial")
        self.caja_fuente.grid(row = 1, column = 1, padx = 25, pady = 5)
        self.caja_fuente.current(135)

        self.caja_tamaño = ttk.Combobox(self.tipo_de_fuente, values = tamañao, justify = CENTER, width = 15, font = "Arial")
        self.caja_tamaño.grid(row = 1, column = 0, padx = 25, pady = 5)
        self.caja_tamaño.current(4)


        self.previo = Label(self.tipo_de_fuente, fg = "black", bg = "SeaGreen1", font = ("Arial", 12))
        self.previo.grid(columnspan=2, row=2, padx=5, pady=25)

        self.aceptar = Button(self.tipo_de_fuente, text = "Aceptar", fg = "black", bg = "white", bd = 2, font =("Arial", 12))
        self.aceptar.grid(columnspan=2, row=3, padx=5, pady=5)

   
    def aceptar(self):
        self.f = str(self.caja_fuente.get())
        self.n = int(self.caja_tamaño.get())
        tipo = (self.f, self.n)
        previo = (self.f, int(self.n*0.7))

        self.previo.config(text = "abc 123", font = (previo) )
        x = self.texto.after(10, self.aceptar)
        if self.click == True:
            self.texto.config(font = tipo)
            self.texto.after_cancel(x)
            self.click = False 
            self.tipo_de_fuente.destroy()

    def color_texto(self):
        color = colorchooser.askcolor()[1]
        self.texto.config(fg = color, insertbackground = color)

    def color_fondo(self):
        color = colorchooser.askcolor()[1]
        self.texto.config(bg = color)

    def crear_archivo(self):
        dirrecion = filedialog.askopenfilename(initialdir ="/", title ="Fichero", filetypes = (("txt files", "*.txt*"),("All files", "*-*")))
        if dirrecion !="":
            fichero = open(fichero, "r")
            contenido = fichero.read()
            self.texto.delete("1.0","end")
            self.texto.insert("1.0",contenido)
            self.master.title(dirrecion)

    def nueva_ventana(self):
        if self.texto.get !="":
            valor = messagebox.askyesno("Bloc de Notas", "¿Deseas guardar el archivo")
            if valor == True:
                self.guardar_archivo()
            else:
                self.texto.delete("1.0", "end")

    def salir(self):
        valor = messagebox.askyesno("Salir", "¿Deseas Salir?")
        if valor == True:   
            self.master.destroy()
            self.master.quit()





if __name__ ==  "__main__":
    ventana = Tk()
    application = Bloc(ventana)
    application.mainloop()
