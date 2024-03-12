notes = [1,6,8,9,10,6,5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]

# Columna 1: Nombre y apellidos (en una única cadena de texto) de cada alumno
# Columna 2: Nota de cada alumno
# Columna 3: Nota "en texto" para cada alumno:
# Si la nota final es inferior a 5, añadir el texto "suspendido".
# Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".
# Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".
# Si la nota es igual o superior a 7, añadir el texto "notable".
# Si la nota supera el 9, añadir el texto "Excelente".
# Si la nota equivale a un 10, añadir el texto "matrícula de honor".
# Columna 4: Diferencia de nota respecto a la mediana del grupo
# Columna 5: Diferencia de nota (expreseda en porcentaje) respecto a la mediana del grupo


# Condiciones especiales
# Antes de hacer los cálculos, debes sumar UN punto a cada alumno, pero la nota máxima nunca puede superar el 10.


# Importamos la librería pandas
import pandas as pd 


# Creamos un dataframe con las listas de alumnos, apellidos y notas
dataframe = pd.DataFrame(
    {
        'Alumne': alumnes, 
        'Cognom': cognoms,
        'Nota': notes
    }
)

dataframe['Alumne'] = dataframe['Alumne'] + ' ' + dataframe['Cognom'] # unimos las columnas de nombre y apellido

# eliminamos la columna de apellidos
dataframe = dataframe.drop(columns=['Cognom'])

dataframe['Nota'] = dataframe['Nota'] + 1 # le suamamos 1 a cada nota

dataframe['Nota'] = dataframe['Nota'].apply(lambda x: 10 if x > 10 else x) # si la nota es mayor que 10, la nota es 10, si no, la nota es la misma

dataframe['Nota en Text'] = dataframe['Nota'].apply(
    lambda x: 'Matrícula de honor' if x == 10 
    else 'Excelente' if x > 9 
    else 'Notable' if x >= 7 
    else 'Bien' if x > 6.1 
     else 'Aprobado' if x >= 5
    else 'Suspendido'
    )
# switch con lambda para las notas en texto


averageOfClass = round(dataframe['Nota'].mean(),2) # media de las notas
dataframe['Diferencia'] = dataframe['Nota'] - averageOfClass  # diferencia de la nota con la mediana

dataframe['Diferencia %'] = dataframe['Diferencia'] / dataframe['Nota'].mean() * 100 # diferencia en porcentaje

# redondear la media a 2 decimales
dataframe['Diferencia %'] = dataframe['Diferencia %'].apply(lambda x: round(x, 2))
print(dataframe)
# download the file as csv
dataframe.to_csv('ex1.csv')