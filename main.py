"""
- Registrar alumnos.
- Generar ficha de matricula.
- Mostrar la lista de todos los matriculados.
- filtrar matriculados por programa de estudios.
"""
lista_alumnos:list=[]
while True:
    opcion:str=input("""------Menu principal------
    escribe (s) si desea agregar un nuevo alumno
    escribe (n) si desea salir del programa
    escribe tu respuesta: """)
    if opcion.lower()=="n":
        break
    while True:
        cui:int=(input("ingrese el numero de dni del alumno: "))
        if cui !="":
            break
        print("es obligatorio ingresar el numero de dni")
    while True:
        nombre:str=input("ingrese el nombre del alumno: ")
        if nombre =="":
            print("es obligatorio ingresar el nombre")
        else:
            break
    apellido:str=input("ingrese el apellido del alumno: ")
    programa_estudio:str=input("ingrese el programa de estudio del alumno: ")
    ciclo:str=input("ingrese el ciclo academico: ")
    nacionalidad:str=input("ingrese su nacionalidad: ")
    fecha_nacimiento:str=input("ingrese su fecha de nacimiento: ")
    numero_celular:int=(input("ingrese el numero de celular: "))
    email:str=input("ingrese su email: ")

    alumno:dict={
        "nombre": nombre,
        "apellido": apellido,
        "programa_estudio": programa_estudio,
        "ciclo": ciclo,
        "nacionalidad": nacionalidad,
        " fecha_nacimiento": fecha_nacimiento,
        "numero_celular": numero_celular,
        "email": email
    }
    lista_alumnos.append(alumno)
print(lista_alumnos)

