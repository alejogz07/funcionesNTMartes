#Funcion para crear una lista de diccionarios
def crear_lista_de_diccionarios(cantidad_estudiantes):
    estudiantes =[]
    for _ in range(cantidad_estudiantes):
        estudiante ={}
        estudiante["id"]=input("id: ")
        estudiante["documento"]=input("documento: ")
        estudiante["esBecado"]=input("esBecado?: ")
        estudiante["nombre"]=input("nombres: ")
    return estudiantes.append(estudiante)
