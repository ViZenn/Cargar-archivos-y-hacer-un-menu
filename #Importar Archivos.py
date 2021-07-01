#Importar Archivos Abriendo Explorador
import os
import pandas as pd
from tkinter.filedialog import askopenfilename

filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
df=pd.read_excel(filename)
df.describe()

print('nueva Rama para el commit')
print('otro print')