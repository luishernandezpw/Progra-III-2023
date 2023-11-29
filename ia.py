#Entrenamiento de una IA para que parenda a convertir temperaturas de celsius a farenheit

import tensorflow as tf
import pandas as pd
#import seaborn as sb

temperaturas = pd.read_csv('temperaturas.csv', sep=";")
#print(temperaturas)

#datos de entrenamiento
celsius = temperaturas["celsius"]
farenheit = temperaturas["farenheit"]

#modelo de entrenamiento, con 1 capa desa oculta
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compilar nuestro modelo
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss="mean_squared_error")

#entrenar el modelo
epocas = modelo.fit(celsius,farenheit,epochs=200, verbose=0)

#probar nuestra Ia
grados = -62
resp = modelo.predict([grados])
print(grados," Grados Celsius son ", resp[0][0], "em fareheit")