import matplotlib.pyplot as plt
import numpy as np

'''
¿Qué es Matplotlib?
Matplotlib es una biblioteca de trazado de gráficos
de bajo nivel en Python que sirve como una utilidad de visualización.

Matplotlib fue creado por John D. Hunter.

Matplotlib es de código abierto y podemos usarlo libremente.

Matplotlib está escrito principalmente en Python,
algunos segmentos están escritos en C, Objective-C y Javascript para compatibilidad con plataformas.
'''

# Graficar un Histograma dado un array de distribución Normal:
'''
Dado un archivo de texto (que contiene una lista de valores de Distribución Normal)
Convertiremos el .txt a array con la libreria numpy para despues graficar por medio de MatPlotlib
un histograma donde se meustre la grafica de distribucion normal

por ultimo la exportaremos la grafica en formato .png
'''

'''
esta vez no leeremos el archivo .txt como hacimos antes con la función open()
en cambio utlizaremos NumPy con metodo .loadtxt('NombreDelArchivo.txt')
asi leerea el automaticamente como un array ahorrando unas lineas de codigo.
'''

dn = np.loadtxt('Distribución_normal_aletoria.txt')
'Visualicemos nuestro array'
print(dn)

# función plt:
'ahora graificaremos la función plot con el metodo .hist retornando un histograma'
'Recordemos que un histograma solo necesita un array de valores.'
plt.hist(dn)
# plt.show() <- si ejecutamos esto antes del .savefig el .png nos aparecera en blanco
plt.title("Distribución Normal (Ejemplo 1)")
plt.grid()
plt.savefig("Dis_norm_plot.png")
plt.close() # cerramos el plot para despues no causar erorores

# Ahora vamos a graficar un grafico de Dispersión:
'''
Con Pyplot, puede usar la scatter()función para dibujar un diagrama de dispersión.

La función scatter()
traza un punto para cada observación.
Necesita dos matrices de la misma longitud,
una para los valores del eje xy otra para los valores del eje y:
'''
## Convertimos el txt en array:
sx = np.loadtxt('Arrays_X_scatter.txt')
sy = np.loadtxt('Arrays_Y_scatter.txt')

## Definimos los coleres del grafico:
'Para Facilitar el codigo, creamos un array que contenga los colores del mismo tamaño del los arrays X & Y'

cols = np.random.randint(100, size=(100))

'Definimos su tamaño'
tam = 10*np.random.randint(100, size=(100))

'Con el metodo .scatter() graficamos la disperción'

plt.scatter(sx,sy, c=cols, s= tam, alpha=0.5, cmap='nipy_spectral')

'Definismos nuestro Grafico que aparezca la barra indicadora de intensidad'
plt.colorbar()

'Guardamos la imagen en .png'
plt.savefig('Grafico_Disperción.png')
'cerramos el archivo apr ano crear problemas con el codigo'
plt.close()
