import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agus
apellido: grandon
---
Ejercicio: entrada_salida_02
---
Simulacro Turno Noche

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. 
Para ello se ingresa por cada ganador:

Nombre
Importe ganado (mayor o igual $1000)
Género (“Femenino”, “Masculino”, “Otro”)
Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

1 Nombre y género de la persona que más ganó.

2 Promedio de dinero ganado en Ruleta.

3 Porcentaje de personas que jugaron en el Tragamonedas.

4 Cuál es el juego menos elegido por los ganadores.

5 El nombre del jugador que ganó más dinero jugando Poker

Texto de la respuesta

Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert

https://onlinegdb.com/qXZHalrNv
https://onlinegdb.com/Eb-b4-h8_
https://onlinegdb.com/UkBoUmbjUF
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #nombre = prompt(title="Pregunta", prompt= "Ingresa tu nombre")
        #alert("Pregunta","Hola"+" "+ nombre)

        desea_continuar = True

        contador_ruleta = 0
        contador_poker = 0
        contador_tragamonedas = 0

        contador_jugadores = 0

        acumulador_ruleta = 0


        while desea_continuar == True:
             
             nombre = prompt("titulo", "ingresa tu nombre")

             importe_ganado = prompt("titulo", "ingresa el importe ganado")
             importe_ganado = int(importe_ganado)
             while importe_ganado <= 1000 :
                 importe_ganado = prompt("titulo", "error, el importe debe ser igual o mayor que $1000")
                 importe_ganado = int(importe_ganado)

             genero = prompt("titulo", "ingresa tu genero")
             while genero != "femenino" and genero != "masculino" and genero != "otro":
               genero = prompt("titulo", "error, ingresa tu genero")

             juego = prompt("titulo", "ingresa el juego")
             while juego != "ruleta" and juego != "poker" and juego != "tragamonedas" :
                 juego = prompt("titulo", "error, ingresa el juego")

             desea_continuar = question("Titulo", "desea continuar")

             #1 Nombre y género de la persona que más ganó.
             if contador_jugadores == 0 or importe_ganado > mayor_jugador :
                 mayor_jugador = importe_ganado
                 nombre_jugador_que_mas_gano = nombre
                 genero_jugador_que_mas_gano = genero
           
        
            #4, Cuál es el juego menos elegido por los ganadores.
             if juego == "ruleta":
                 contador_ruleta += 1
                 if juego == "ruleta":
                     acumulador_ruleta += importe_ganado   
             elif juego == "poker":
                 contador_poker += 1
                  #5 El nombre del jugador que ganó más dinero jugando Poker
                 if contador_jugadores == 0 or importe_ganado > mayor_jugador :
                  mayor_jugador = importe_ganado
                  nombre_jugador_que_mas_gano_jugando_poker = nombre
             else:
                contador_tragamonedas += 1
            
             contador_jugadores += 1

       
        #3Porcentaje de personas que jugaron en el Tragamonedas.
        porcentaje_de_personas_que_jugaron_al_tragamonedas =  (contador_tragamonedas * 100) / contador_jugadores

        #2 Promedio de dinero ganado en Ruleta.  
        #esto si no se ingresa nada me da error
        if contador_ruleta > 0:
           promedio_de_ruleta = acumulador_ruleta / contador_ruleta
        else:
           promedio_de_ruleta = "no se ingresaron jugadores de ruleta"



        #punto cuatro comparacion:
        if contador_ruleta < contador_poker and contador_ruleta < contador_tragamonedas:
            juego_menos_elegido = "ruleta"
        elif contador_poker < contador_tragamonedas:
            juego_menos_elegido = "poker"
        else:
            juego_menos_elegido = "tragamonedas"

        mensaje = (f"el juego menos elegido es {juego_menos_elegido}.\n"
                   f"el nombre de la persona que mas dinero ganor es {nombre_jugador_que_mas_gano}, y su genero es {genero_jugador_que_mas_gano}.\n"
                   f"el promedio de dinero ganado en ruleta es {promedio_de_ruleta}.\n"
                   f"el porcentaje de personas que jugaron en el tragamonedas es {porcentaje_de_personas_que_jugaron_al_tragamonedas}%.\n"
                   f"nombre del jugador que mas gano jugando poker {nombre_jugador_que_mas_gano_jugando_poker}")
        alert("titulo", mensaje)

                 
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()