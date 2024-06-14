import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: Listas_conteo
---
Enunciado:
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

Bonus:
    i. El listado de numeros pares
    j. Que se ingreso mas? positivos, negativos o ceros

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista_numeros = []

    def btn_comenzar_ingreso_on_click(self):
        lista = []
        contador_general = 0
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_negativos = 0
        contador_positivos = 0
        cantidad_de_ceros = 0
        bandera_minimo = False
        bandera_maximo = False

        while contador_general < 5:
            numeros = input("ingresa un numeros:  ")
            numeros = int(numeros)
            lista.append(numeros)
            print(lista)
            contador_general += 1
        
        for numero in lista:
            if numero == 0:
                cantidad_de_ceros += 1
            elif numero < 0:
                contador_negativos += 1
                acumulador_negativos += numero
            else:
                contador_positivos += 1
                acumulador_positivos += numero

            if bandera_minimo == False or numero < numero_minimo:
                numero_minimo = numero
                bandera_minimo = True
            if bandera_maximo == False or numero > numero_maximo:
                numero_maximo = numero
                bandera_maximo = True

        if contador_negativos > 0:
            promedio_negativos = (acumulador_negativos / contador_negativos) 
        else:
            print("no se puede dividir por 0")


        mensaje = (f"la suma de negativos es {acumulador_negativos}\n"
                  f"la suma de positivos es {acumulador_positivos}\n"
                  f"la cantidad de numeros positivos es {contador_positivos}\n"
                  f"la cantidad de numeros negativos es {contador_negativos}\n"
                  f"la cantidad de ceros es {cantidad_de_ceros}\n"
                  f"el numero minimo es {numero_minimo}\n"
                  f"el numero maximo es {numero_maximo}\n"
                  f"el promedio de numeros negativos es {promedio_negativos}")
        
        print(mensaje)

        
    def btn_mostrar_estadisticas_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
