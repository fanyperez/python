# 1. Los compañeros del día 5 estamos en una lotería donde el premio a repartir es de 1,000,000.
#    A cada compañero, le toca una parte del premio de manera aleatoria.
#
# 2. Además del monto del premio, a cada participante de manera aleatoria se le asigna un país destino
#    para gastar su premio.

# Genear un archivo de Excel con Python donde aparezcan los participantes del día 5, el monto que ganó de la lotería y
# el destino que le tocó.
#
# Lo que se espera: En el archivo Excel, la primera columna debe tener los nombres de todos los participantes.
# En la segunda columna, poner el monto que cada quien obtuvo de manera aleatoria del premio.
# En la tercera columna, debe reflejarse el país que se le asignó de manera aleatoria.
# Cada columna debe llevar un header (Nombre | Monto | País destino)

# Usar listas
# Leer el archivo txt de los nombres
# Usar random()
# Usar pycountry para generar el país
# Usar openpyxl para exportar datos a excel

import pycountry
import random

with open('lista.txt', "r") as e:
     names = [i for i in e]

# converts a number to a column letter. from openpyxl.utils import get_column_letter .
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()

dest_filename = 'excel.xlsx'

ws = wb.active

ws.title = "Dia 5"

ws['A1'] = 'Name'
row = 2
column = 1 
for i in names:
     ws.cell(row=row, column=column).value = i 
     row += 1

ws['B1'] = 'Moneyss'
row = 2
column =2

def num_pieces(num,lenght):
    ot = list(range(1,lenght+1))[::-1]
    all_list = []
    for i in range(lenght-1):
        n = random.randint(1, num-ot[i])
        all_list.append(n)
        num -= n
    all_list.append(num) 
    return all_list

dineros = num_pieces(1000000,len(names))
#print(milista)

for i in range (len(names)):
       ws.cell(row=row, column=column).value = dineros[i]
       row += 1

ws['C1'] = 'Country'
row = 2
column = 3
for i in range (len(names)):
     prueba = (random.choice(list(pycountry.countries)))
     p2 = prueba.name
     ws.cell(row=row, column=column, value = p2) #.value = i
     row += 1

     
wb.save(filename = dest_filename)
