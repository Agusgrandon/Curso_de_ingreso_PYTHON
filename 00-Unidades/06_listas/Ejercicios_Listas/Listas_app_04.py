
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_04
---
Enunciado:
Al presionar el botón 'INGRESAR' se le solicitará al usuario que ingrese:
    Edad.
    Genero.
Luego del ingreso, al presionar el boton 'INFORMAR' mostrar por Dialog Alert:
    A. Promedio de edad de los hombres.
    B. Porcentaje de mujeres mayores de 18 respecto al total de personas. 
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

        for i in range(5):
            edad = input("ingresa tu edad:  ")
            edad = int(edad)
            genero = input("ingresa tu genero:  ")
            edades.append(edad)
            generos.append(genero)
            contador_general += 1
            print(contador_general)

            if genero == "m":
                contador_hombres += 1
                acumulador_edad_hombres += edad

            if genero == "f" and edad >= 18:
                contador_mujeres += 1

        promedio = acumulador_edad_hombres / contador_hombres
        porcentaje = (contador_mujeres * 100) / contador_general
        mensaje = f"el promedio de edad es {promedio}, el porcentaje de mujeres es {porcentaje}"
        print(mensaje) 
   


        contador_general = 0
        contador_hombres = 0
        acumulador_edad_hombres = 0
        contador_mujeres = 0

        while contador_general < 5:
            edad = input("ingresa tu edad:  ")
            edad = int(edad)
            genero = input("ingresa tu genero:  ")
            edades.append(edad)
            generos.append(genero)

            #COMO RECORRER LAS DOS LISTAS
            for i in range(len(edades)):
                for j in range(len(generos[i])):
                    if genero[j] == "m":
                        contador_hombres += 1
                        acumulador_edad_hombres += edades[i]
                    
                    if genero[j] == "f" and edad[i] > 18:
                        contador_mujeres += 1
            
            contador_general += 1
                
        promedio_edad_hombres = acumulador_edad_hombres / contador_hombres
        porcentaje_de_mujeres = (contador_mujeres * 100) / contador_general
        mensaje = f"La edad promedio de los hombres es {promedio_edad_hombres}, y el porcentaje de mujeres {porcentaje_de_mujeres}"
        print(mensaje)


        

    def btn_informar_on_click(self):
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()