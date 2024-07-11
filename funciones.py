import random, os
os.system("cls")

trabajadores = ['Juan Pérez ' , 'María García', 'Carlos López' , 'Ana Martínez', 'Pedro Rodríguez','Laura Hernández', 'Miguel Sánchez', 'Isabel Gómez' ,'Francisco Díaz','Elena Fernández']
sueldo_traba = []


def asignar_sueldos_aleatorios():
   for t in range(len(trabajadores)):
    sueldo_random = random.randint(300000,2500000)
    sueldo_traba = trabajadores[t], sueldo_random
    trabajadores.append(sueldo_traba)
    print(sueldo_traba)


def Clasificar_sueldos():
 for t in range(len(sueldo_traba)):
    total = 0
    total_sueldos = 0
    if sueldo_traba[t][-1] <= 800000:
      print(f"sueldos menores a 800000 {sueldo_traba[t][-1]}, total: {total}")
      total = total + 1 
      total = total_sueldos

      

      
      

    


def ver_estadisticas():
  pass

def reporte_de_sueldos():
  import csv
  for t in range(trabajadores):
    print(sueldo_traba[t])
  with open("nombre_archivo".csv , "x", newline="") as archivo:
    escritor = csv.DictWriter(archivo)


    


def salir_del_programa():
  print("finalizando programa...")
  print("Desarrollador por Scarleth Perez")
  print("RUT 21.475.201-8")
  exit()

  



