import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_01
---
Enunciado:
Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en la lista_datos utilizando Dialog Alert para informar cada elemento.
(Utilizar 'for in range' y 'for in')

for i in range(lista):
Este código itera sobre los índices de una lista, utilizando la función range() para generar una secuencia de
números que van desde 0 hasta el tamaño de la lista menos uno. Luego, en cada iteración, accedes a los 
elementos de la lista utilizando el índice i. 

for elemento in lista:
Este código itera directamente sobre los elementos de la lista, sin necesidad de usar índices. 
En cada iteración, elemento tomará el valor de uno de los elementos de la lista. 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]

    def btn_mostrar_on_click(self):
        lista = [2,3,5,7,11,13]

        for numeros in lista:
            print(numeros)   
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()