import os
from pathlib import Path
import shutil  #Libreria que permite eliminar un directorio con contenido
import contenidoArchivos as ca
from os import system

def crear_directorios():
    directorio = Path(Path.home(),"Recetas")
    if not Path.exists(directorio):
        os.makedirs(directorio)
    else:
        shutil.rmtree(directorio)  #Elimino el directorio Recetas el cual va a contener sub-directorios y archivos

    lista_categorias = ["Carnes","Ensaladas","Pastas","Postres"]

    for i in lista_categorias:
        os.makedirs(Path(directorio,i))  #Se crean los sub-directorios con el nombre de la lista

    return directorio

def crear_archivos(directorio,estructura_inicial):
    subDirectorios = os.listdir(directorio) #Creo una lista con todos los Sub-directorios de Recetas
    for i in estructura_inicial.keys():
        for y in estructura_inicial[i]:
            archivo = open(Path(directorio,i)/f"{y}.txt","a")
            receta = getattr(ca, y) #Se hace uso de esta funcion para poder concatenar el alias del modulo con el nombre de la variable a llamar
            archivo.write(receta)
            archivo.close()

def bienvenida(directorio):
    categorias = os.listdir(directorio)
    print(f"""                          BIENVENIDO A TU RECETARIO
        La ruta donde a sido creada la carpeta es {directorio}
Actualmente el recetario cuenta con las siguientes categorias: {categorias}
    """)

def leer_receta(directorio):
    system("cls")
    categorias = os.listdir(directorio)
    for i in enumerate(categorias):
        print(f"{i[0] + 1} - {i[1]}")
    opcion = input("Escribe el nombre de alguna de las categorias: ")
    if Path(directorio,opcion).exists():
        system("cls")
        recetas = os.listdir(Path(directorio,opcion))
        for i in enumerate(recetas):
            print(f"{i[0] + 1} - {i[1]}")
        archivo = input("Escribe el nombre del archivo de la receta: ")
        receta_archivo = open(Path(directorio,opcion,archivo))
        print(receta_archivo.read())
        receta_archivo.close()
    else:
        print("Opcion INCORRECTA")
        system("cls")
        leer_receta(directorio)

def crear_receta(directorio):
    system("cls")
    categorias = os.listdir(directorio)
    for i in enumerate(categorias):
        print(f"{i[0] + 1} - {i[1]}")
    opcion = input("Escribe el nombre de la categoria donde vas a crear la receta: ")
    if Path(directorio,opcion).exists():
        system("cls")
        nombre_receta = input("Por favor escriba el nombre de la receta: ")
        system("cls")
        receta = input("Escriba a continuacion la receta: ")
        system("cls")
        desicion = input("Esta seguro de crear el archivo con la informacion antes proporcionada?(Si/No): ")
        if desicion.lower() == "si":
            nueva_receta = open(Path(directorio,opcion,f"{nombre_receta.title().replace(' ','')}.txt"),"w")
            nueva_receta.write(receta)
            nueva_receta.close()
            system("cls")
            print("Receta Creada")
            input()
    else:
        print("Opcion INCORRECTA")
        system("cls")
        leer_receta(directorio)

def crear_categoria(directorio):
    system("cls")
    nueva_categoria = input("Ingrese el nombre de la nueva categoria: ")
    system("cls")
    desicion = input("Esta seguro de crear el archivo con la informacion antes proporcionada?(Si/No): ")
    if desicion.lower() == "si":
        if Path(directorio, nueva_categoria).exists():
            system("cls")
            print("La categoria ya existe no puede ser creada")
        else:
            os.makedirs(Path(directorio,nueva_categoria))
            print("La Categoria ha sido CREADA")
            input()

def eliminar_receta(directorio):
    system("cls")
    categorias = os.listdir(directorio)
    for i in enumerate(categorias):
        print(f"{i[0] + 1} - {i[1]}")
    categoria = input("Escribe el nombre de alguna de las categorias: ")
    if Path(directorio,categoria).exists():
        system("cls")
        recetas = os.listdir(Path(directorio,categoria))
        for i in enumerate(recetas):
            print(f"{i[0] + 1} - {i[1]}")
        receta = input("Escribe el nombre de la receta a eliminar: ")
        system("cls")
        desicion = input(f"Esta seguro de eliminar la receta {receta}?(Si/No): ")
        if desicion.lower() == "si":
            if Path(directorio, categoria, receta).exists():
                system("cls")
                os.remove(Path(directorio, categoria,receta))
                print("La receta ya fue ELIMINADA")
                input()
            else:
                print("La receta NO EXISTE")
                input()
    else:
        print("Opcion INCORRECTA")
        system("cls")
        leer_receta(directorio)

def eliminar_categoria(directorio):
    system("cls")
    categoria = input("Ingrese el nombre de la categoria a eliminar: ")
    system("cls")
    desicion = input(f"Esta seguro de eliminar la categoria {categoria}?(Si/No): ")
    if desicion.lower() == "si":
        if Path(directorio, categoria).exists():
            system("cls")
            shutil.rmtree(Path(directorio, categoria))
            print("La categoria ya fue ELIMINADA")
            input()
        else:
            print("La Categoria NO EXISTE")
            input()


#El diccionario a continuacion es la estructura inicial las claves son subdirectorios de Recetas y los valores son archivos
estructura_inicial = {
    "Carnes":["recetaEtrecotAlMalbec", "recetaMatambrePizza"],
    "Ensaladas":["recetaEnsaladaGriega", "recetaEnsaladaMediterranea"],
    "Pastas":["recetaCanelonesDeEspinaca", "recetaRaviolesDeRicotta"],
    "Postres":["recetaCompotaDeManzana", "recetaTartaDeFrambuesas"]
}
raiz_recetas = crear_directorios()
crear_archivos(raiz_recetas,estructura_inicial)
bienvenida(raiz_recetas)
while True:
    opcion = input("Por favor introduce una opcion: ")
    match opcion:
        case "1":
            leer_receta(raiz_recetas)
        case "2":
            crear_receta(raiz_recetas)
        case "3":
            crear_categoria(raiz_recetas)
        case "4":
            eliminar_receta(raiz_recetas)
        case "5":
            eliminar_categoria(raiz_recetas)
        case  "6":
            break
        case _:
            print("Por Favor Introduzca una opcion CORRECTA")

print("!! GRACIAS !!")
