# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=6, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        self.lista_nombre = ["Pepe", "Paola", "Dardo", "Fatiga", "Maria"]
        self.lista_monto = [20000,30000,40000,50000,60000]
        self.lista_tipo_instrumento = ["CEDEAR","BONOS","MEP","CEDEAR","CEDEAR"]
        self.lista_cantidad_instrumento = [20, 35, 199, 100, 80]
    
    def btn_cargar_datos_on_click(self):
        contador_ventas = 0
        contador_BONOS = 0
        contador_CEDEAR = 0
        contador_MEP = 0
        acumulador_mep = 0
        acumulador_CEDEAR = 0


        while contador_ventas <= 3 :
            nombre = prompt("Titulo", "Ingresa tu nombre")
            while nombre == None or nombre == '':
                nombre = prompt("Titulo", "Error, ingresa tu nombre")
            #Monto en pesos de la operación (no menor a $10000)
            monto_de_operacion = prompt("Titulo", "Ingresa el monto de la opreacion")
            monto_de_operacion = int(monto_de_operacion)
            while monto_de_operacion < 10000 :
                monto_de_operacion = prompt("Titulo", "Error, ingresa un monto mayor a $10.000")
                monto_de_operacion = int(monto_de_operacion)
            #Tipo de instrumento(CEDEAR, BONOS, MEP)
            tipo_de_instrumento = prompt("Titulo", "Ingresa el instrumento: CEDEAR, BONOS, MEP")
            while tipo_de_instrumento != "CEDEAR" and tipo_de_instrumento != "BONOS" and tipo_de_instrumento != "MEP" :
                tipo_de_instrumento =prompt("Titulo", "Error, ingresa el instrumento: CEDEAR, BONOS, MEP")
            # Cantidad de instrumentos  (no menos de cero)
            cantidad_de_instrumento = prompt("Titulo", "Ingresa la cantidad de instrumentos")
            cantidad_de_instrumento = int(cantidad_de_instrumento)
            while cantidad_de_instrumento < 0 :
                cantidad_de_instrumento = prompt("Titulo", "Error, ingresa la cantidad de instrumentos")
                cantidad_de_instrumento = int(cantidad_de_instrumento)
            
            #0) - Tipo de instrumento que menos se operó en total.
            if tipo_de_instrumento == "CEDEAR" :
                contador_CEDEAR += 1 
                ##! 3) - Cantidad de usuarios que no compraron CEDEAR 
                if cantidad_de_instrumento == 0 :
                     acumulador_CEDEAR += 1
            elif tipo_de_instrumento == "BONOS" :
                contador_BONOS += 1
            else:
                contador_MEP += 1
                ##! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
                if cantidad_de_instrumento > 50 and cantidad_de_instrumento < 200 :
                    acumulador_mep += 1

            


            contador_ventas += 1
        ##! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
        promedio_instrumentos_mep = cantidad_de_instrumento / contador_MEP
        
        ##! 8) - Promedio de dinero en CEDEAR  ingresado en total.
        if contador_CEDEAR < 0 :
            promedio_cedear = monto_de_operacion / contador_CEDEAR 
        else: 
            promedio_cedear = "no se puede dividir por 0"
        ##! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
               
        #MAXIMO
        if contador_CEDEAR > contador_BONOS and contador_CEDEAR> contador_MEP:
            instrumento_mas_votado = "CEDEAR"
        elif contador_BONOS > contador_MEP:
            instrumento_mas_votado = "BONOS"
        else:
            instrumento_mas_votado = "MEP"
        #MINIMO 
        if contador_CEDEAR < contador_BONOS and contador_CEDEAR < contador_MEP:
            instrumento_menos_votado = "CEDEAR"
        elif contador_BONOS < contador_MEP:
            instrumento_menos_votado = "BONOS"
        else:
            instrumento_menos_votado = "MEP"

        mensaje = (f"El instrumento más votado fue {instrumento_mas_votado}.\n"
                   f"El instrumento menos votado es {instrumento_menos_votado}.\n"
                   f"la cantidad de usuarios que compraron entre 50 y 200MEP son {acumulador_mep}.\n"
                   F"la cantidad de usuarios que no compraron CEDEAR son {acumulador_CEDEAR}.\n"
                   f"el promedio de dinero invertido en cedear es {promedio_cedear}.\n"
                   f"el promedio de cantidad de instrumentos MEP vendidos son {promedio_instrumentos_mep}")

        alert("Titulo", mensaje)






    def btn_mostrar_informe_1(self):
        pass
        


    def btn_mostrar_informe_2(self):
        pass
        


    def btn_mostrar_informe_3(self):
        pass      


    def btn_mostrar_todos_on_click(self):
        pass

        

if __name__ == "__main__":
    app = App()
    app.mainloop()
