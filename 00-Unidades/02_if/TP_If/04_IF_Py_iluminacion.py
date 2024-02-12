import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agus
apellido: grandon
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        cantidad = self.combobox_cantidad.get()
        cantidades = float(cantidad)
        marca = self.combobox_marca.get()
        importe = cantidades * 800

        # Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%. 
        descuento_cincuenta = importe * 50 / 100 
        descuento_uno = importe - descuento_cincuenta

        # Si compra 5 lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % 
        descuento_cuarenta = importe * 40 / 100 
        descuento_dos = importe - descuento_cuarenta

        # si es de otra marca el descuento es del 30%.
        descuento_treinta = importe * 30 / 100
        descuento_tres = importe - descuento_treinta

        # Si compra 4 lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % 
        descuento_veinticinco = importe * 25 / 100
        descuento_cuatro =  importe - descuento_veinticinco

        # y si es de otra marca el descuento es del 20%.
        descuento_veinte = importe * 20 / 100 
        descuento_cinco = importe - descuento_veinte

        # Si compra 3 lamparitas bajo consumo marca "ArgentinaLuz" el descuento es del 15%
        descuento_quince = importe * 15 / 100
        descuento_seis = importe - descuento_quince

        # si es “FelipeLamparas” se hace un descuento del 10% 
        descuento_diez = importe * 10 / 100
        descuento_siete = importe - descuento_diez

        # y si es de otra marca un 5%
        descuento_cincoo = importe * 5 / 100
        descuento_ocho = importe - descuento_cincoo

        # Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
        importe_dos = importe * 5 / 100
        descuento_final = importe - importe_dos
 

        if cantidades >= 6 :
            alert("Titulo", descuento_uno)
        elif cantidades == 5 : 
             if marca == "ArgentinaLuz" :
                alert("Titulo", descuento_dos)
             else :
                alert("Titulo", descuento_tres)
        elif cantidades == 4 :
             if (marca == "ArgentinaLuz" or marca == "FelipeLamparas") :
                alert("Titulo", descuento_cuatro)
             else : 
                alert("Titulo", descuento_cinco)
        elif cantidades == 3 : 
             if marca == "ArgentinaLuz" :
                alert("Titulo", descuento_seis)
             elif marca == "FelipeLamparas" :
                alert("Titulo", descuento_siete)
             else :
                alert("Titulo", descuento_ocho)
        elif importe == 4000 :
            alert("Titulo", descuento_final)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()