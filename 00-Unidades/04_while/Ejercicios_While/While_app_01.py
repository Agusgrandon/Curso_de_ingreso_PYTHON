import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: agus
apellido: grandon
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
# UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
# que promete revolucionar el mercado. 
# Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 


# Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

# Los datos a ingresar por cada encuestado son:
#     * nombre del empleado
#     * edad (no menor a 18)
#     * genero (Masculino - Femenino - Otro)
#     * tecnologia (IA, RV/RA, IOT)   

# En esta opción, se ingresaran empleados hasta que el usuario lo desee.

# Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

# '''



class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        #contador_inicial = 1
        #while contador_inicial <= 10:
            #alert("Titulo", contador_inicial)
            #contador_inicial += 1
        
        #antes del while
        continuar = True
        contador_m_tec = 0
        contador_tec_IA = 0
        contador_tec_RV_RA= 0
        contador_tec_IOT = 0
        contador_f = 0
        contador_m = 0
        contador_otro = 0
        contador_f_IA = 0
        acumulador_f_IA = 0




        #durante el whiel, adentro sumamos, contamos, afuera comparamos
        while continuar == True:
                    
            nombre = input("Ingresa tu nombre") #si no se pide validarlo, no se valida
            edad = input("Ingresa tu edad")
            edad = int(edad)
            while edad < 18 : 
                edad = input("Error, ingresa tu edad")
                edad = int(edad)
            
            genero = input( "Ingresa tu genero")
            while genero != "masculino" and genero != "femenino" and genero != "otro" :
                genero = input( "Error, ingresa tu genero")
            
            tecnologia = input("Ingresa la tecnologia")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT" :
                tecnologia = input( "Error, Ingresa la tecnologia")

            continuar = question("Titulo","Desea continuar?")
            
            #ej2: maximo, tiene que ir afuera porque primero tenemos que ver el contador, y despues afuera lo comparo
            if tecnologia == "IA":
                contador_tec_IA += 1
            elif tecnologia == "RV/RA":
                contador_tec_RV_RA += 1
                 #ej6: HALLAR MINIMO
                if contador_tec_RV_RA == 1 or edad < edad_minima :
                    edad_minima = edad
                    nombre_minimo = nombre
                    genero_minimo = genero
            else:
                contador_tec_IOT += 1
                if (edad >= 18 and edad <=25) or (edad >= 33 and edad <= 42 ):
                    contador_tec_IOT += 1

            
            #ej3: sacar porcentaje 
            match genero:
                case "femenino":
                    contador_f += 1
                    if tecnologia == "IA" :
                       contador_f_IA += 1
                       acumulador_f_IA += edad
                case "masculino":
                    contador_m += 1
                    #ej1: contador, primero lee los and, por eso el or va en parentesis
                    if (tecnologia == "IA" or tecnologia == "IA") and edad >= 25 and edad <= 50 :
                      contador_m_tec += 1
                case "otro":
                    contador_otro += 1



        #despues del while
        #ej2comparacion:
        if contador_tec_IOT > contador_tec_IA and contador_tec_IOT > contador_tec_RV_RA:
            tecnologia_mas_votada = "IOT"
        elif contador_tec_IA > contador_tec_RV_RA :
            tecnologia_mas_votada = "IA"
        else:
            tecnologia_mas_votada = "RV/RA"
        #ej 3
        total_empleados = contador_f + contador_m + contador_otro
        porcentaje_femenino = (contador_f * 100) / total_empleados
        porcentaje_masculino = (contador_f * 100) / total_empleados
        porcentaje_otro = 100 - (porcentaje_femenino + porcentaje_masculino)
        #ej4:
        porcetaje_IOT = (contador_tec_IOT * 100) / total_empleados
        #ej5:
        if contador_f_IA > 0:
           promedio_femenino_IA = acumulador_f_IA / contador_f_IA 
        else:
            promedio_femenino_IA = "no se puede dividir por 0"



        print(f"cantidad masculinos IOT/IA en rango de edad es: {contador_m_tec}")
        print(f"la tec más votada  es: {tecnologia_mas_votada}")
        print(f"porcentaje femenino{porcentaje_femenino}, mas{porcentaje_masculino}, otro{porcentaje_otro}")
        print(f"porcentaje votaron IOT en rango {porcetaje_IOT}")
        print(f"promedio f que vootaron IA {promedio_femenino_IA}")
        if contador_tec_RV_RA != 0:
         print(f"minimo{edad_minima}, {genero_minimo }, {nombre_minimo}")
        else:
            print("no se encontro el minimo")
              
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()