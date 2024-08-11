import tkinter as tk
from tkinter import ttk
import math

def calcular_presupuesto():
    try:
        metros = float(entrada_metros.get())
        ancho_rachola = float(entrada_ancho.get())
        alto_rachola = float(entrada_alto.get())
        coste_rachola = float(entrada_coste.get())
        
        area_rachola = (ancho_rachola / 100) * (alto_rachola / 100)
        racholas_necesarias = math.ceil(metros / area_rachola)
        coste_total = racholas_necesarias * coste_rachola
        
        resultado.set(f"Racholas necesarias: {racholas_necesarias}\nCoste total: {coste_total:.2f}€")
    except ValueError:
        resultado.set("Por favor, introduce valores numéricos válidos.")

def calcular_yeso():
    if var_yeso.get():
        try:
            metros = float(entrada_metros.get())
            coste_saco = float(entrada_coste_yeso.get())
            
            sacos_necesarios = math.ceil(metros / 5)
            coste_total_yeso = sacos_necesarios * coste_saco
            
            resultado_yeso.set(f"Sacos de yeso necesarios: {sacos_necesarios}\nCoste total del yeso: {coste_total_yeso:.2f}€")
        except ValueError:
            resultado_yeso.set("Por favor, introduce valores numéricos válidos.")
    else:
        resultado_yeso.set("")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Reforma")

# Variables
resultado = tk.StringVar()
resultado_yeso = tk.StringVar()
var_yeso = tk.BooleanVar()

# Frame para el cálculo de racholas
frame_racholas = ttk.LabelFrame(ventana, text="Cálculo de Racholas")
frame_racholas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

ttk.Label(frame_racholas, text="Metros cuadrados:").grid(row=0, column=0, sticky="w")
entrada_metros = ttk.Entry(frame_racholas)
entrada_metros.grid(row=0, column=1)

ttk.Label(frame_racholas, text="Ancho de rachola (cm):").grid(row=1, column=0, sticky="w")
entrada_ancho = ttk.Entry(frame_racholas)
entrada_ancho.grid(row=1, column=1)

ttk.Label(frame_racholas, text="Alto de rachola (cm):").grid(row=2, column=0, sticky="w")
entrada_alto = ttk.Entry(frame_racholas)
entrada_alto.grid(row=2, column=1)

ttk.Label(frame_racholas, text="Coste por rachola (€):").grid(row=3, column=0, sticky="w")
entrada_coste = ttk.Entry(frame_racholas)
entrada_coste.grid(row=3, column=1)

ttk.Button(frame_racholas, text="Calcular", command=calcular_presupuesto).grid(row=4, column=0, columnspan=2)
ttk.Label(frame_racholas, textvariable=resultado).grid(row=5, column=0, columnspan=2)

# Frame para el cálculo de yeso
frame_yeso = ttk.LabelFrame(ventana, text="Cálculo de Yeso")
frame_yeso.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

ttk.Checkbutton(frame_yeso, text="Calcular yeso", variable=var_yeso, command=calcular_yeso).grid(row=0, column=0, columnspan=2)

ttk.Label(frame_yeso, text="Coste por saco de yeso (€):").grid(row=1, column=0, sticky="w")
entrada_coste_yeso = ttk.Entry(frame_yeso)
entrada_coste_yeso.grid(row=1, column=1)

ttk.Label(frame_yeso, textvariable=resultado_yeso).grid(row=2, column=0, columnspan=2)

ventana.mainloop()
