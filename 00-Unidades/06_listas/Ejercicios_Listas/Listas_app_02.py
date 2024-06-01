import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_02
---
Enunciado:
Al presionar el botón 'Calcular' se deberá sumar todos los numeros de la lista, mostrar el resultado de la sumatoria y el promedio por Dialog Alert . 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]
        
    def btn_calcular_on_click(self):
        lista = len(self.lista_datos)
        acumulador = 0
        contador = 0

        for i in range(lista):
            contador += 1
            for j in range(self.lista_datos[i]):
                acumulador += j
          
        if contador > 0:
            division = acumulador / contador
 
        mensaje = f"la sumatoria es {acumulador}, y el promedio es {division}"
        alert("titulo", mensaje)
    

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()