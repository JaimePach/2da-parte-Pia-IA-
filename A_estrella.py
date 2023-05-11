import csv
import os
import time
from os import system

folder = 'C:\\Users\\jg823\\OneDrive\\Documentos\\A estrella IA\\'
datos = []

system("cls")

def asignar_Instancias(Archivo):
    print('_________________' + Archivo + ' ___________________')

    subtema = []
    tarea = []
    duracion = []
    valor = []
    obligatorio = []
    requerimiento1 = []
    requerimiento2 = []

    with open(folder + 'low-dimensional\\' + Archivo, 'rt') as t:
        reader = csv.reader(t)
        for row in reader:
            if len(row) > 0:
                if row[0] != '':
                    subtema.append(int(row[2]))
                    tarea.append(int(row[3]))
                    duracion.append(int(row[4]))
                    valor.append(int(row[5]))
                    requerimiento1.append(int(row[7]))
                    requerimiento2.append(int(row[8]))
                    obligatorio.append(int(row[9]))
    return [subtema, tarea, duracion, valor, obligatorio, requerimiento1, requerimiento2]

def Breadth_First_Search(Datos):
    tareasCompletadas = []
    califSubtema = [0, 0, 0, 0, 0, 0, 0, 0]
    duracionSubtema = [0, 0, 0, 0, 0, 0, 0, 0]

    for subtemaActual in range(0, 8, 1):
        for tareaActual in range(0, 11, 1):
            if Datos[4][subtemaActual * 11 + tareaActual] == 1:
                tareasCompletadas.append(subtemaActual * 11 + tareaActual)
                califSubtema[subtemaActual] += Datos[3][subtemaActual * 11 + tareaActual]
                duracionSubtema[subtemaActual] += Datos[2][subtemaActual * 11 + tareaActual]

                if Datos[5][subtemaActual * 11 + tareaActual] != 0:
                    tareasCompletadas.append(Datos[5][subtemaActual * 11 + tareaActual])
                    califSubtema[Datos[0][Datos[5][subtemaActual * 11 + tareaActual]] - 1] += Datos[3][
                        Datos[5][subtemaActual * 11 + tareaActual]]
                    duracionSubtema[Datos[0][Datos[5][subtemaActual * 11 + tareaActual]] - 1] += Datos[2][
                        Datos[5][subtemaActual * 11 + tareaActual]]

                if Datos[6][subtemaActual * 11 + tareaActual] != 0:
                    tareasCompletadas.append(Datos[6][subtemaActual * 11 + tareaActual])
                    califSubtema[Datos[0][Datos[6][subtemaActual * 11 + tareaActual]] - 1] += Datos[3][
                        Datos[6][subtemaActual * 11 + tareaActual]]
                    duracionSubtema[Datos[0][Datos[6][subtemaActual * 11 + tareaActual]] - 1] += Datos[2][
                        Datos[6][subtemaActual * 11 + tareaActual]]        
                                 # Algoritmo informado
        while califSubtema[subtemaActual] < 70:
            mejorRelacion = 0
            mejorTarea = None

            for tarea in range(0, 11):
                tareaIndex = subtemaActual * 11 + tarea

                if tareaIndex not in tareasCompletadas:
                    valor = Datos[3][tareaIndex]
                    duracion = Datos[2][tareaIndex]

                    if duracionSubtema[subtemaActual] + duracion <= 100:
                        relacion = valor / duracion

                        if relacion > mejorRelacion:
                            mejorRelacion = relacion
                            mejorTarea = tareaIndex

            if mejorTarea is None:
                break

            tareasCompletadas.append(mejorTarea)
            califSubtema[subtemaActual] += Datos[3][mejorTarea]
            duracionSubtema[subtemaActual] += Datos[2][mejorTarea]

            if Datos[5][mejorTarea] != 0:
                tareasCompletadas.append(Datos[5][mejorTarea])
                califSubtema[Datos[0][Datos[5][mejorTarea]] - 1] += Datos[3][Datos[5][mejorTarea]]
                duracionSubtema[Datos[0][Datos[5][mejorTarea]] - 1] += Datos[2][Datos[5][mejorTarea]]

            if Datos[6][mejorTarea] != 0:
                tareasCompletadas.append(Datos[6][mejorTarea])
                califSubtema[Datos[0][Datos[6][mejorTarea]] - 1] += Datos[3][Datos[6][mejorTarea]]
                duracionSubtema[Datos[0][Datos[6][mejorTarea]] - 1] += Datos[2][Datos[6][mejorTarea]]

    print("\nLas Tareas a completar son las siguientes:\n", tareasCompletadas)
    print("\nLas Calificaciones de cada subtema son:\n", califSubtema)
    print("\nLa Duración de cada subtema es:\n", duracionSubtema)

# Resto del código sin cambios

Start = time.time()

for archivo in os.listdir(folder + 'low-dimensional\\'):
    if archivo.endswith(".csv"):
        separador = archivo.split('_')
        datos = asignar_Instancias(archivo)
        resultadoFinal = Breadth_First_Search(datos)

        datos = []

runtime = time.time() - Start
print("Runtime: " + str("{:.15f}".format(runtime)) + "\n")