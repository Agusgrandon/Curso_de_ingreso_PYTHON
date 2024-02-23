import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agus
apellido: grandon
---
Ejercicio: while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        #la bandera me sirve para , solo se cambia el valor de la bandera si el if fue mayor a 10 if var >10:
        #me avisa que el numero que se ingreso fue 10 o menor es una iteracion, me avisa que la variable fue o no mayor o igual a 10
        #me avisa d ecambios de estados especifios o genericos
        #continuar = question("hola", "quiere continuar")
        # PARA MAX: 
        #contador = 0
        #if contador == 0 or edad > edad_maxima
        #edad_maxima = edad
        #sumatoria_edad += edad
        #contador += 1
        flag = True

        while True:
            numero = prompt("Titulo", "Ingrese un numero")
            if numero == None :
                break

            numero = int(numero)

            if flag == True : #aca pregunto si 0 es el primero, para saber si estamos en la primera vuelta, y aca hacemos la primera asignacion
                maximo = numero #ceteamos las variables por primera vez
                minimo = numero #evaluo cual es el max y mini y lo guardo en la variable
                flag = False
            else:
                if numero > maximo : #aca pregunto si el numero ingresado es max o minimo
                    maximo = numero
                elif numero < minimo :
                    minimo = numero
            

        self.txt_minimo.delete(0, "end")
        self.txt_minimo.insert(0, minimo)

        self.txt_maximo.delete(0, "end")
        self.txt_maximo.insert(0, maximo)

#se empieza con el contador, en el if se evalua el numero ingresado, 
# cosas que no se tienen que hacer: no se puede declarar en variables el mx y min, y despues preguntar con el if
# el elif es el SI NO del otro lado, es la negacion de la primer pregunta 
# concepto de las banderas: flag, se puede usar para preguntar algo, se reemplaza por el contador, ej flag = true, pregunto si es igual a treu, y despues coloco flase
# la bandera me sirve para separar cosas, tengo que ponerla al final por que si no siempre me va a tomar el primer numero       
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
