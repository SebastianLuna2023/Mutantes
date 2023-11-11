
print("Bienvenido al Programa Mutantes")
print("--------------------------")
print("El mismo sera compuesto de 6 filas y 6 columnas")
print("Se ingresara la primer fila compuestoa por 6 letras "
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
