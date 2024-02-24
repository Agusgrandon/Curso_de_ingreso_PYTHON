import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agus
apellido: ggrandon
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_de_votos = 0
        candidato_mas_votado = 0
        continuar = True

        while continuar == True :

            nombre_del_candidato = prompt("Titulo", "Ingresa el nombre del candidato")
            if nombre_del_candidato == None or nombre_del_candidato == '':
                nombre_del_candidato = prompt("Titulo", "Ingresa el nombre del candidato")
            
            edad_del_candidato = prompt("Titulo", "Ingresa la edad del candidato")
            edad_del_candidato = int(edad_del_candidato)
            if edad_del_candidato == '' or edad_del_candidato < 25 :
                edad_del_candidato = prompt("Titulo", "Ingresa la edad del candidato")
                edad_del_candidato = int(edad_del_candidato)
            
            cantidad_de_votos = prompt("Titulo", "Ingresa la cantidad de votos que recibio")
            cantidad_de_votos = int(cantidad_de_votos)
            if cantidad_de_votos == None or cantidad_de_votos < 0 :
                cantidad_de_votos = prompt("Titulo", "Ingresa la cantidad de votos que recibio")
                cantidad_de_votos = int(cantidad_de_votos)
            
            continuar = question("Titulo", "Desea continuar?")
        
            #d. total de votos emitidos.
            contador_de_votos += cantidad_de_votos
            #a. nombre del candidato con más votos
            if cantidad_de_votos :
                candidato_mas_votado += 1

        if cantidad_de_votos > candidato_mas_votado:
            candidato_mas_votado = cantidad_de_votos


        mensaje = f"La cantidad de votos es {contador_de_votos}, el candidato más votado es {candidato_mas_votado}"
        alert("Titulo", mensaje)

            
            

           

          






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
