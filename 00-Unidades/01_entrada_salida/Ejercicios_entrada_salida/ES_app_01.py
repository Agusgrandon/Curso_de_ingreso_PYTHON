import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agus 
apellido: grandon
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''
'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        desea_continuar = True
        general = 16000
        campo = 25000
        platea = 30000
        descuento = 0

        while desea_continuar == True :
            nombre = prompt("Titulo", "ingresa tu nombre")

            edad = prompt("Titulo", "ingresa tu edad")
            edad = int(edad)
            while edad < 16 :
                edad = prompt("Titulo", "error, ingresa tu edad")
                edad = int(edad)
            
            genero = prompt("Titulo", "ingresa tu genero")
            while genero != "masculino" and genero != "femenino" and genero != "otro" :
                genero = prompt("Titulo", "error, ingresa tu genero")

            tipo_de_entrada = prompt("Titulo", "selecciona la ubicacion") 
            while tipo_de_entrada != "general" and tipo_de_entrada != "campo" and tipo_de_entrada != "platea" :
                tipo_de_entrada = prompt("Titulo", "error, selecciona la ubicacion")

            medio_de_pago = prompt("Titulo", "selecciona el medio de pago")
            while medio_de_pago != "debito" and medio_de_pago != "efectivo" and medio_de_pago != "credito" :
                medio_de_pago= prompt("Titulo", "error, el medio de pago")

            desea_continuar = question("titulo","desea continuar?")
            
            match tipo_de_entrada :
                case "general":
                    if medio_de_pago == "debito" :
                        descuento = 15
                        descuento_a_realizar = (descuento * general) / 100
                    elif medio_de_pago == "credito" :
                        descuento = 20
                        descuento_a_realizar = (descuento * general) / 100
                case "campo":
                    if medio_de_pago == "debito" :
                        descuento = 15
                        descuento_a_realizar = (descuento * campo) / 100
                    elif medio_de_pago == "credito" :
                        descuento = 20
                        descuento_a_realizar = (descuento * campo) / 100
                case "platea":
                    if medio_de_pago == "debito" :
                        descuento = 15
                        descuento_a_realizar = (descuento * platea) / 100
                    elif medio_de_pago == "credito" :
                        descuento = 20
                        descuento_a_realizar = (descuento * platea) / 100



        descuento_hecho = general - descuento_a_realizar 

        mensaje = f"el precio final es {descuento_hecho}"
        alert("titulo", mensaje)

   


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
