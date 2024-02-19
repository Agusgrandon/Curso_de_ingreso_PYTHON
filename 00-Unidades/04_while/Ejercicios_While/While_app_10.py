import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agus 
apellido: grandon
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        positivos = 0
        negativos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
  
        while True :
            numeros = prompt("Titulo", "Ingresa un numero")

            if numeros == None:
                break
            numero = int(numeros)
            if numero < 0 :
                negativos += numero
                cantidad_negativos += 1
            elif numero > 0 :
                positivos += numero 
                cantidad_positivos += 1
            elif numero == 0 :
                cantidad_ceros += 1

        
        diferencia = cantidad_positivos - cantidad_negativos
        mensaje = f"El resultado es {positivos}, {negativos}, {cantidad_positivos}, {cantidad_negativos}, {cantidad_ceros}, {diferencia}"
        alert("Titulo", mensaje)




    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
