import random, os, time
os.system("cls")

from funciones import*


while True:
    os.system("cls")
    print("MENÚ")
    print("---------------------------------------")
    print("1. Asignar sueldos aleatorios ")
    print("2. Clasificar sueldos ")
    print("3. ver estadísticas ")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    print("---------------------------------------")
    opc = int(input("Ingrese opción: "))

    if opc==1:
        asignar_sueldos_aleatorios()
    elif opc==2:
        Clasificar_sueldos()
    elif opc==3:
        ver_estadisticas()
    elif opc==4:
        reporte_de_sueldos()
    elif opc==5:
        salir_del_programa()
    else:
        print("ERROR! opción incorrecta!")
    time.sleep(5)
