import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agus
apellido: grandon
---
Ejercicio: entrada_salida_03
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener el contenido de la caja de texto para luego 
mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
       #mostrarNombre = self.txt_nombre.get()
       #alert("Titulo","Hola"+" "+ mostrarNombre)
        
       #OTRO: Porcentaje de dinero en función de cada juego
        
        # Nombre y género de la persona que más ganó.
        contador_ganadores = 0

        # Promedio de dinero ganado en Ruleta.
        contador_ruleta = 0
        contador_poker = 0
        contador_tragamonedas = 0

        # Promedio de dinero ganado en Ruleta.
        acumulador_ruleta = 0
        flag = True
        while flag:
            # Nombre
            nombre = prompt("CASINO", "Ingrese nombre de ganador")
            while nombre == None or nombre == "":
                nombre = prompt("CASINO", "Reingrese nombre de ganador")

            # Importe ganado (mayor o igual $1000)
            importe = prompt("CASINO", "Ingrese el importe ganado")
            while importe == None or importe == "" or float(importe) < 1000:
                importe = prompt("CASINO", "Reingrese el importe ganado")
            importe = float(importe)

            # Género (“Femenino”, “Masculino”, “Otro”)
            genero = prompt("CASINO", "Ingrese el genero")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("CASINO", "Reingrese el genero")

            # Juego (Ruleta, Poker, Tragamonedas)
            juego = prompt("CASINO", "Ingrese el juego")
            while juego != "Ruleta" and juego != "Poker" and juego !="Tragamonedas":
                juego = prompt("CASINO", "Reingrese el juego")

            match(juego):
                case "Ruleta":
                    # Promedio de dinero ganado en Ruleta.
                    contador_ruleta += 1
                    acumulador_ruleta += importe
                case "Poker":
                    contador_poker += 1
                    # El nombre del jugador que ganó más dinero jugando Poker
                    if contador_poker == 1 or mayor_importe_poker < importe:
                        mayor_importe_poker = importe
                        nombre_mayor_importe_poker = nombre
                case _:
                    contador_tragamonedas += 1

            # Nombre y género de la persona que más ganó.
            if contador_ganadores == 0 or mayor_importe < importe:
                mayor_importe = importe
                nombre_mayor_ganador = nombre
                genero_mayor_ganador = genero
            
            contador_ganadores += 1
            flag = question("CASINO", "Desea continuar?")
            
        # Nombre y género de la persona que más ganó.
        mensaje = f"Jugador que mas gano es {nombre_mayor_ganador} y su genero es {genero_mayor_ganador}\n"

        # Promedio de dinero ganado en Ruleta.
        if contador_ruleta > 0:
            promedio_ruleta = acumulador_ruleta / contador_ruleta
            mensaje += f"El promedio del dinero ganado en ruleta es {promedio_ruleta}\n"
        else:
            mensaje += f"No se ingresaron ganadores de ruleta\n"
            
        # Porcentaje de personas que jugaron en el Tragamonedas.
        if contador_tragamonedas > 0:
            porcentaje_jugadores_tragamoneda = (contador_tragamonedas * 100) / contador_ganadores
            mensaje += f"El porcentaje de personas que jugaron al Tragamonedas es {porcentaje_jugadores_tragamoneda}%\n"
        else:
            mensaje += f"No hubo jugadores de Tragamonedas\n"

        # Cuál es el juego menos elegido por los ganadores.
        if contador_poker < contador_ruleta and contador_poker < contador_tragamonedas:
            mensaje += f"El juego menos elegido por los jugadores es Poker\n"
        elif contador_tragamonedas < contador_ruleta:
            mensaje += f"El juego menos elegido por los jugadores es Ruleta\n"
        else:
            mensaje += f"El juego menos elegido por los jugadores es Tragamonedas\n"

        # El nombre del jugador que ganó más dinero jugando Poker
        if contador_poker > 0:
            mensaje += f"El jugador que mas gano dinero jugando Poker es: {nombre_mayor_importe_poker}"
        else:
            mensaje += f"No se ingresaron jugadores de poker"
        alert("CASINO", mensaje)
            

                
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()