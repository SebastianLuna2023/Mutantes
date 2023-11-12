print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("Bienvenido al Programa Mutantes")
print("--------------------------")
print("El mismo sera compuesto de 6 filas y 6 columnas")
print("Se ingresara la primer fila compuesta por 6 letras "
    "y luego la segunda hasta completar")
print("No olvidar que las letras que componen el codigo o "
    "fila son: `A, T, C, G` unicamente ")
print("--------------------------------------")

dna = []



def verficarLetra(fila, indice = 0):
    letrasValidas = ["A", "T", "C", "G"]
    if indice < len(fila):
        letra = fila[indice]
        if letra not in letrasValidas:
            print("Letra no Valida")
            return False
        return verficarLetra(fila, indice + 1)
    return True
        


contadorFila = int(0)
while contadorFila < 6:
    
    contadorFila +=1
    
    fila = ""
    print("--------------------------------------")
    print("RECUERDE: 6 caracteres: A, T, C, G" )
    print("--------------------------------------")
    
    filaValida = False

    while not filaValida:

        fila = input(f"Ingrese fila {contadorFila}: ")
        fila = fila.upper()

        if len(fila) < 6:
            print("DEBE INGRESAR 6 CARACTERES")
        elif len(fila) > 6:
            print("DEBE INGRESAR SOLAMENTE 6 CARACTERES")

        if len(fila) == 6 and verficarLetra(fila):
            filaValida = True
        
        
    dna.append(list(fila))

print("El codigo genetico ingresado es: ")

for fila in dna:
    for elemento in fila:
        print(elemento, end= " ")
    print()

# VERIFICAR SI EXISTEN MUTANTES:

#Condicion Mutante: 
# Sabrás si un humano es mutante, 
# si encuentras MAS DE UNA SECUNCIA de cuatro letras iguales, 
# de forma oblicua, horizontal o vertical.



def isMutant(dna):
    contadorSecuencias = 0

    for filaADN in dna:
        filaSecuencia = 0
        for indice in range(len(filaADN) - 1):
            if filaADN[indice] == filaADN[indice + 1]:
                filaSecuencia += 1
                if filaSecuencia == 3:
                    contadorSecuencias += 1
                    break
            else:
                filaSecuencia = 0
    

    for indiceColumna in range(len(dna[0])):
        columnaSecuencia = 0
        for indiceFila in range(len(dna) - 1):
            if dna[indiceFila][indiceColumna] == dna[indiceFila + 1][indiceColumna]:
                columnaSecuencia += 1
                if columnaSecuencia == 3:
                    contadorSecuencias += 1
                    break
            else:
                filaSecuencia = 0
    

    for indiceColumna in range(len(dna[0]) - 1):
        diagonalSecuencia = 0
        for indiceFila in range(len(dna) - 1):
            if dna[indiceFila][indiceColumna] == dna[indiceFila + 1][indiceColumna + 1]:
                diagonalSecuencia += 1
                if diagonalSecuencia == 3:
                    contadorSecuencias += 1
                    break
            else:
                diagonalSecuencia = 0
    

    for indiceColumna in reversed(range(1, len(dna[0]))):
        diagonalIzquierda = 0
        for indiceFila in reversed(range(len(dna) - 1)):
            if indiceColumna - indiceFila >= 0:
                if dna[indiceFila][indiceColumna] == dna[indiceFila + 1][indiceColumna - 1]:
                    diagonalIzquierda += 1
                    if diagonalIzquierda == 3:
                        contadorSecuencias += 1
                        break
                else:
                    diagonalIzquierda=0
    

    return contadorSecuencias >= 2
    
    
print("--------------------------------------")

print("--------------------------------------")



if isMutant(dna):
    print("El DNA contiene el gen MUTANTE!!!!!")
    print("--------------------------------------")
else:
    print("No se encontro gen mutante")
    print("--------------------------------------")
    