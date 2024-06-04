import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_05
---
Enunciado:
Al presionar el botón 'INGRESAR' se le solicitará al usuario que ingrese:
    Edad - Validar (Entre 15 y 90 años).
    Genero - Validar (Femenino/Masculino/No Binario).
Luego del ingreso, al presionar el boton 'INFORMAR' mostrar por Dialog Alert:
    A. Promedio de edad de los masculinos.
    B. Porcentaje de femeninos mayores de 18 respecto al total de personas.
    C. Porcentaje de personas de cada genero.
    D. Informar edad y genero de la persona con menor edad, puede ser mas de una.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label = customtkinter.CTkLabel(master=self, text="Edad")
        self.label.grid(row=0, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Genero")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        self.txt_genero = customtkinter.CTkEntry(master=self)
        self.txt_genero.grid(row=1, column=1)

        self.btn_ingresar = customtkinter.CTkButton(master=self, text="INGRESAR", command=self.btn_ingresar_on_click)
        self.btn_ingresar.grid(row=2, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(master=self, text="INFORMAR", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=3, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.lista_edades = []
        self.lista_generos = []


    def btn_ingresar_on_click(self):
        edades = []
        generos = []
        acumulador_edad_hombres = 0
        contador_hombres = 0
        contador_general = 0
        contador_mujeres = 0
        bandera = False

        

        for i in range(5):
            edad = input("Ingresa tu edad: ")
            edad = int(edad)
            while edad < 15 or edad > 90:
                edad = input("Error, reingresa tu edad: ")
                edad = int(edad)
            genero = input("Ingresa tu genero:  ")
            while genero != "f" and genero != "m" and genero != "nb":
                genero = input("Error, reingresa tu genero:  ")

            edades.append(edad)
            generos.append(generos)
            contador_general += 1

            if genero == "m":
                contador_hombres += 1
                acumulador_edad_hombres += edad
            if genero == "f" and edad >= 18:
                contador_mujeres += 1


        edad_minima = edades[0]
        edad_maxima = edades[0]
        for i in range(len(edades)):
            if bandera == False or edades[i] < edad_minima:
                edad_minima = edades[i]
                #genero_minimo = generos[i]
                bandera = True
            if edades[i] > edad_maxima:
                edad_maxima = edades[i]
                #genero_maximo = generos[i]

        promedio_edad_hombres = acumulador_edad_hombres / contador_hombres
        porcentaje = (contador_mujeres * 100) / contador_general
        mensaje = f"el promedio de edad es {promedio_edad_hombres}, el porcentaje de mujeres es {porcentaje}, la edad minima es {edad_minima}, y la edad max es {edad_maxima}"
        print(mensaje) 


    def btn_informar_on_click(self):
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()