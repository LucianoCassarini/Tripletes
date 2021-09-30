
#===========================Auxiliares=================================

#devuelve nombre del usuario
def name(line):
    posicion = line.find(",")
    return line[0:posicion]

#devuelve página visitada
def pag(line):
    posicion1 = line.find(",")
    aux = line[(posicion1+1):]
    pos2 = aux.find(",")
    return aux[(pos2+1):]

#Comprobar si el triplete está contenido en una lista dada
def comprobar(triplete, lista):
    for i in range(0, (len(lista))):
        if triplete[0] == lista[i]:
            n = i
            n += 1
            if n < len(lista):
                if triplete[1] == lista[n]:
                    n += 1
                    if n < len(lista):
                        if triplete[2] == lista[n]:
                            return True
    return False

#Comprueba todas las apariciones de los tripletes de una lista en una lista de listas
def comprobarLista(list1, List2):
    tripleteList = []

    for i in range(0, (len(list1))):
        if i < (len(list1) - 2):
            n = i
            triplete = [list1[n]]
            n += 1
            triplete.append(list1[n])
            n += 1
            triplete.append(list1[n])
            contador = 1
            for j in List2:
                if comprobar(triplete, j):
                    contador += 1
            tripleteList.append([triplete, contador])
    return tripleteList

#Crear lista de apariciones de cada triplete
def aparicion(lista):
    listaApariciones = []
    for i in range(0, (len(lista))):
        l1 = lista[i]
        n = i
        n += 1
        LL = lista[n:]
        listaApariciones.append(comprobarLista(l1, LL))
    #Quitar corchetes extra
    Limpia = []
    for l in listaApariciones:
        for x in l:
            Limpia.append(x)
    return Limpia

#Elimina los elementos repetidos
def eliminarRepetidos(LL):
    LLaux = []
    for i in range(0, len(LL)):
        bandera = False
        for x in LLaux:
            if (LL[i])[0] == x[0]:
                bandera = True
        if bandera == False:
            LLaux.append(LL[i])
    return LLaux

#devuelve el triplete que aparece con mayor frecuencia
def buscarMayor(LL):
    mayor = 0
    mayorTriplete = []
    indexMayor = 0
    for i in range(0, len(LL)):
        if (LL[i])[1] > mayor:
            mayor = (LL[i])[1]
            mayorTriplete = (LL[i])[0]
            indexMayor = i

    LL.pop(indexMayor)
    return mayorTriplete

#Retorna una lista con el top 10 tripletes más comunes, desde el más al menos recurrente
def top10(LL):
    top = []
    for i in range(0, 9):
        if len(LL) != 0:
            top.append(buscarMayor(LL))
    return top

#==================================================== MAIN ====================================================

#-------------Import de archivo---------------
from io import open

archivo_text = open("docText.txt", "r")

lineas_texto = archivo_text.readlines()

archivo_text.close()

#----------------------------------
LUsuarios = []

#Crea una tupa con los usuarios
for x in lineas_texto:
    aux = name(x)
    if aux not in LUsuarios:
        LUsuarios.append(aux)

Usuarios = tuple(LUsuarios)

#Crea una lista compuesta por la lista de paginas que recorre cada usuario
ListaAuxiliar = []

for x in Usuarios:
    auxList = []
    for y in lineas_texto:
        if name(y) == x:
            auxList.append(str.strip(pag(y)))
    ListaAuxiliar.append(auxList)

listaApariciones = aparicion(ListaAuxiliar)

listaApariciones = eliminarRepetidos(listaApariciones)

TOP = top10(listaApariciones)

print(TOP)

