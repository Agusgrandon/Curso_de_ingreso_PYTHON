import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        
        for numero in range(1):
            numero = input("ingresa un numero: ")
            numero = int(numero)

            if numero % 1 and numero % numero:
                mensaje = f"el numero {numero} es primo"
            else:
                mensaje = f"el numero {numero} no es primo"

            print(mensaje)

        numero = input("Ingresa un numero")
        numero = int
        es_primo = True

        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break

        
        if es_primo:
            print(f"{numero} es un numero primo")
        else:
            print(f"{numero} no es un numero primo")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()