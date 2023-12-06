import os
from pathlib import Path
import shutil  #Libreria que permite eliminar un directorio con contenido
import contenidoArchivos as ca
import importlib

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

#El diccionario a continuacion es la estructura inicial las claves son subdirectorios de Recetas y los valores son archivos
estructura_inicial = {
    "Carnes":["recetaEtrecotAlMalbec", "recetaMatambrePizza"],
    "Ensaladas":["recetaEnsaladaGriega", "recetaEnsaladaMediterranea"],
    "Pastas":["recetaCanelonesDeEspinaca", "recetaRaviolesDeRicotta"],
    "Postres":["recetaCompotaDeManzana", "recetaTartaDeFrambuesas"]
}
raiz_recetas = crear_directorios()
crear_archivos(raiz_recetas,estructura_inicial)