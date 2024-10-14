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

lista_alumnos:list=[]

def mensaje_menu():
    menu_opciones="""------Menu principal------
    escribe (s) si desea agregar un nuevo alumno
    escribe (n) si desea salir del programa
    escribe tu respuesta: """
    return menu_opciones

def ingresar_datos_alumnos():
    id=len(lista_alumnos)+1
    cui:str=input("ingrese el numero de dni del alumno: ")
    nombre:str=input("ingrese el nombre del alumno: ")
    apellido:str=input("ingrese el apellido del alumno: ")
    programa_estudio:str=input("ingrese el programa de estudio del alumno: ")
    ciclo:str=input("ingrese el ciclo academico del alumno: ")
    numero_celular:int=input("ingrese el numero de celular: ")
    email:str=input("ingrese su email: ")
    guardar_datos_alumnos(id,cui,nombre,apellido,programa_estudio,ciclo,numero_celular,email)

def guardar_datos_alumnos(id,cui,nombre,apellido,programa_estudio,ciclo,numero_celular,email):
    alumno:dict={
        "id":id,
        "cui":cui,
        "nombre": nombre,
        "apellido": apellido,
        "programa_estudio": programa_estudio,
        "ciclo": ciclo,
        "numero_celular": numero_celular,
        "email": email
    }
    lista_alumnos.append(alumno)

while True:
    menu_opciones=input(mensaje_menu())
    if menu_opciones.lower()=="n":
        print("saliendo del programa...")
        break
    elif menu_opciones.lower()=="s":
        ingresar_datos_alumnos()
    else:
        print("opcion errroea")
print(lista_alumnos)