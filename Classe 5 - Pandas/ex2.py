# Planteamiento del problema
# En este dataset tienes los datos extraídos del canal de YouTube "KEXP" en formato xlsx. La "KEXP" (Seattle International) es una emisora con una larga tradición de conciertos en directo. El dataset contiene todos los vídeos publicados hasta el 11/03/2024. Queremos saber:

# Volumnen general: ¿Cuantas filas y columnas tiene el dataset completo?
# Composición del dataset: ¿Qué columnas componen el dataset?
# Calcula la desviación (abs y percent) de cada vídeo sobre el promedio de especatadores/comentarios/likes del canal.
# Localiza el vídeo más visto.
# Localiza el vídeo más comentado.
# Crea una nueva columna para cada uno de los valores calculador anteriormente, y crea un nuevo dataset final que incorpore toda la nueva información.
# Calcula la duración en segundos de cada video, e indica su desviación percent sobre el promedio de duración de los videos del canal.
# Visualiza todas las estadísticas calculadas anteriormente en un gráfico de Tableau
import pandas as pd 

data = pd.read_csv('kexp.csv')

print(data.tail())


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"1. Volumen Genera: El dataset tiene", data.shape[0], 'filas y', data.shape[1], 'columnas')

print(f"2. Composición del dataset: Las columnas que componen el dataset son: ")
for i,v in enumerate(data.columns):
    print(i, ': ',v)

# 0 :  id
# 1 :  publishedAt
# 2 :  channelId
# 3 :  channelTitle
# 4 :  categoryId
# 5 :  title
# 6 :  description
# 7 :  tags
# 8 :  viewCount
# 9 :  likeCount
# 10 :  commentCount
# 11 :  duration
# 12 :  blocked_at
# 3

print(f"3. Desviación abs y percent de cada vídeo sobre el promedio de espectadores, comentarios y likes del canal: ")
averageViews = data['viewCount'].mean()
averageComments = data['commentCount'].mean()
averageLikes = data['likeCount'].mean()

data['Desviación abs Views'] =averageViews  - data['viewCount']
data['Desviación abs Comments'] =averageComments -  data['commentCount']
data['Desviación abs Likes'] =averageLikes  -data['likeCount'] 

data['Desviación percent Views'] = data['viewCount'] - averageViews / averageViews * 100
data['Desviación percent Comments'] = data['commentCount'] / averageComments / averageComments * 100
data['Desviación percent Likes'] = data['likeCount'] / averageLikes / averageLikes * 100

print(data[['Desviación abs Views', 'Desviación percent Views', 'Desviación abs Comments', 'Desviación percent Comments', 'Desviación abs Likes', 'Desviación percent Likes']])





print(bcolors.OKGREEN , "Mean likes " ,  averageLikes , bcolors.ENDC)
print(bcolors.OKCYAN , "Mean comments " ,  averageComments , bcolors.ENDC)
print(bcolors.OKBLUE , "Mean views " ,  averageViews , bcolors.ENDC)




# Localiza el vídeo más visto.
print(bcolors.OKGREEN , "4. El vídeo más visto es: ",  averageViews , bcolors.ENDC)
print(data[data['viewCount'] == data['viewCount'].max()]['title'])
# Localiza el vídeo más comentado.
print(bcolors.OKCYAN , "4. El vídeo más comentado es: ",  averageViews , bcolors.ENDC)
print(data[data['commentCount'] == data['commentCount'].max()]['title'])


# Calcula la duración en segundos de cada video, e indica su desviación porcentual sobre el promedio de duración de los videos del canal.

# Input = PT2M57S , Output = 177 (seconds) HINT: Puedes usar expresiones regulares para extraer los números de la cadena de texto.
# From youtube API time to seconds 
def durationToSeconds(duration):
    duration = duration.replace('PT', '') # remove PT    
    hours = 0
    minutes = 0
    seconds = 0
    
    if 'H' in duration:
        hours = int(duration.split('H')[0])
        duration = duration.split('H')[1]
    if 'M' in duration:
        minutes = int(duration.split('M')[0])
        duration = duration.split('M')[1]
    if 'S' in duration:
        seconds = int(duration.split('S')[0])
    return hours * 3600 + minutes * 60 + seconds



data['duration'] = data['duration'].apply(durationToSeconds)
print(data['duration'])

averageDuration = data['duration'].mean()

data['Desviación percent Duration'] = data['duration'] / averageDuration / averageDuration * 100

print(data['Desviación percent Duration'])


data.to_csv('ex2.csv')