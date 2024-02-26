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
        contador_candidatos = 0
        contador_edades = 0 
        continuar = True

        while continuar == True :

            nombre_del_candidato = prompt("Titulo", "Ingresa el nombre del candidato")
            while nombre_del_candidato == None or nombre_del_candidato == '':
                nombre_del_candidato = prompt("Titulo", "Ingresa el nombre del candidato")
            
            edad_del_candidato = prompt("Titulo", "Ingresa la edad del candidato")
            edad_del_candidato = int(edad_del_candidato)
            while edad_del_candidato < 25 :
                edad_del_candidato = prompt("Titulo", "Ingresa la edad del candidato")
                edad_del_candidato = int(edad_del_candidato)
            
            cantidad_de_votos = prompt("Titulo", "Ingresa la cantidad de votos que recibio")
            cantidad_de_votos = int(cantidad_de_votos)
            while cantidad_de_votos == '' or cantidad_de_votos < 0 :
                cantidad_de_votos = prompt("Titulo", "Ingresa la cantidad de votos que recibio")
                cantidad_de_votos = int(cantidad_de_votos)
            #a. nombre del candidato con más votos
            if contador_candidatos == 0 or cantidad_de_votos > mayor_votado :
                mayor_votado = cantidad_de_votos
                candidato_mas_votado = nombre_del_candidato
            #b nombre y edad del candidato con menos votos
            if contador_candidatos == 0 or cantidad_de_votos < menor_votado :
                menor_votado = cantidad_de_votos
                candidato_menos_votado = nombre_del_candidato
                edad_del_candidato_menos_votado = edad_del_candidato

            
            continuar = question("Titulo", "Desea continuar?")
        
            #d. total de votos emitidos.
            contador_de_votos += cantidad_de_votos
            contador_candidatos += 1
            contador_edades += edad_del_candidato
            
        

        #c. el promedio de edades de los candidatos
        promedio_edad = contador_edades / contador_candidatos
        mensaje = (
            f"La cantidad de votos es {contador_de_votos}.\n"
            f"el candidato más votado es {candidato_mas_votado}.\n"
            f"el candidadto menos votados es {candidato_menos_votado}, y su edad es {edad_del_candidato_menos_votado}.\n"
            f"el promedio de edad entre los candidatos es {promedio_edad}")
        alert("Titulo", mensaje)

            
            

           

          






if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
