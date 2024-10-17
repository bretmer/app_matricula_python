lista_alumnos:list=[]

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
def mostrar_alumnos():
    return lista_alumnos