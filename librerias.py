import pandas as pd

#leer el archivo de notas.csv
notas = pd.read_csv("notas.csv", sep=";", encoding="utf-8")
#print(notas)

#Obtener las notas sobresalientes.
sobresalientes = notas.loc[notas["notas"]>=9]
#print(sobresalientes)

#obtener las los estudiantes quw reprobaron 
reprobados = notas.loc[notas["notas"]<6]
#print(reprobados)

#Contar cuantos han reprobado
cantidad_reprobados = notas.loc[notas["notas"]<6].agg({"count"})
#print(cantidad_reprobados)

#agrupar por nota
agrupados = notas.groupby(["notas"]).agg({"sum"})
print(agrupados)