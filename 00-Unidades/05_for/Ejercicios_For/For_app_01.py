import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: agustina isabel
apellido: grandon
---
Ejercicio: parcial
---
Enunciado:
Al presionar el botón Mostrar 5 veces un mensaje (utilizando el Dialog Alert) con números ASCENDENTES, desde el 1 al 5.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_contenedores = 0
        #Informe A- Cuál fue la categoría menos ingresada (peligroso, comestible, indumentaria)
        contador_peligroso = 0
        contador_comestible = 0
        contador_indumentaria = 0
        #Informe B- El porcentaje de contenedores por Tipo de material ( aluminio, hierro , madera)
        contador_aluminio = 0
        contador_hierro = 0
        contador_madera = 0
        #Informe E- El promedio de peso de todos los contenedores
        acumulador_contenedores = 0
        

        while contador_contenedores < 20 :
               
               marca = prompt("titulo", "Ingresa la marca del contenedor")
               

               categoria = prompt("titulo", "Ingresa la categoria: ")
               while categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria":
                    categoria = prompt("titulo", "error, ingresa la categoria: ")
                
               peso = prompt("titulo", "Ingresa el peso: ")
               peso = int(peso)
               while peso < 100 or peso > 800 :
                    peso = prompt("titulo", "error, igresa el peso: ")
                    peso = int(peso)

               tipo_de_material = prompt("titulo", "ingrese el tipo de material")
               while tipo_de_material != "aluminio" and tipo_de_material != "hierro" and tipo_de_material != "madera" :
                    tipo_de_material = prompt("titulo", "error, ingrese el tipo de material")

               costo = prompt("titulo", "ingresa el costo")
               costo = int(costo)
               while costo < 1 :
                    costo = prompt("titulo", "erro, ingresa el costo")
                    costo = int(costo)

               match categoria :
                    case "peligroso":
                         contador_peligroso += 1
                         #Informe D- La marca del contenedor peligroso con mayor costo
                         if contador_peligroso == 1 or costo > contenedor_con_mayor_costo :
                              contenedor_con_mayor_costo = costo
                              marca_contenedor_con_mayor_costo = marca 
                         else:
                              marca_contenedor_con_mayor_costo = "no se ingreso nada"
                    case "comestible":
                         contador_comestible += 1
                    case "indumentaria":
                         contador_indumentaria += 1   

               match tipo_de_material :
                    case "aluminio":
                         contador_aluminio += 1
                    case "hierro":
                         contador_hierro += 1
                    case "madera":
                         contador_madera += 1

               #Informe C- La marca y tipo del contenedor menos pesado
               if contador_contenedores == 0 or peso < contenedor_menos_pesado :
                    contenedor_menos_pesado = peso
                    marca_contenedor_menos_pesado = marca
                    tipo_contenedor_menos_pesado = tipo_de_material
                
               acumulador_contenedores += peso
               contador_contenedores += 1

        #Informe A- Cuál fue la categoría menos ingresada (peligroso, comestible, indumentaria)
        if contador_peligroso < contador_indumentaria or contador_peligroso < contador_comestible :
             categoria_menos_ingresada = "peligroso"
        elif contador_comestible < contador_indumentaria:
             categoria_menos_ingresada = "comestible"
        else:
             categoria_menos_ingresada = "indumentaria"

        #Informe B- El porcentaje de contenedores por Tipo de material ( aluminio, hierro , madera)
        porcentaje_aluminio = (contador_aluminio * 100) / contador_contenedores
        porcentaje_hierro = (contador_hierro * 100) / contador_contenedores
        porcentaje_madera = (contador_madera * 100) / contador_contenedores

        #Informe E- El promedio de peso de todos los contenedores
        promedio_de_peso = acumulador_contenedores / contador_contenedores 

        mensaje = (f"la categoria menos ingresada fue {categoria_menos_ingresada}.\n"
                   f"el porcentaje de contenedores de aluminio es {porcentaje_aluminio}%, el porcentaje de hierro es {porcentaje_hierro}%, el porcentaje de madera es {porcentaje_madera}%.\n"
                   f"la marca del contenedor menos pesado es {marca_contenedor_menos_pesado}, y el tipo es {tipo_contenedor_menos_pesado}.\n"
                   f"La marca del contenedor peligroso con mayor costo es {marca_contenedor_con_mayor_costo}.\n"
                   f"El promedio de peso de todos los contenedores {promedio_de_peso}")
        print(mensaje)
             
             
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()