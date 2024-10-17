"""
- Registrar alumnos.
- Generar ficha de matricula.
- Mostrar la lista de todos los matriculados.
- filtrar matriculados por programa de estudios.
"""
# lista_alumnos:list=[]
# while True:
#     opcion:str=input("""------Menu principal------
#     escribe (s) si desea agregar un nuevo alumno
#     escribe (n) si desea salir del programa
#     escribe tu respuesta: """)
#     if opcion.lower()=="n":
#         break
#     nombre:str=input("ingrese el nombre del alumno: ")
#     apellido:str=input("ingrese el apellido del alumno: ")
    
#     alumno:dict={
#         "nombre": nombre,
#         "apellido": apellido
#     }
#     lista_alumnos.append(alumno)
# print(lista_alumnos)

from menu import mensaje_menu
from datos_alumnos import ingresar_datos_alumnos, mostrar_alumnos

while True:
    menu_opciones=input(mensaje_menu())
    if menu_opciones.lower()=="n":
        print("saliendo del programa...")
        break
    elif menu_opciones.lower()=="s":
        ingresar_datos_alumnos()
    else:
        print("opcion errroea")
print(mostrar_alumnos())
