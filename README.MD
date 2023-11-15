# Mutants
* Nombre y Apellido: Sebastián Luna
* Email: sebas16_2003@hotmail.com
* Registro: 51588 

## Proyecto Mutantes

El presente proyecto es un desafío planteado por la cátedra de Programación 1, materia dictada en la Universidad Tecnológica Nacional regional Cuyo.

El código escrito pide al usuario ingresar por consola cadenas de 6 caracteres que formarán una matriz de 6x6. Posteriormente, se valida que distintas combinaciones, ya sea de forma oblicua, horizontal o vertical, no repitan letras.

Si cumple con esta condición, el sistema arrojará como resultado que se encontró ADN mutante.

## Dificultades

*Actualmente, se plantea utilizar la menor cantidad de bucles y en su lugar utilizar recursividad, así como también evitar el uso de librerías.
*Adicionalmente agregue el recorrido de diagonal invertida 

## Testeo

Deberan ingresar una por una las filas a medida el sistema se los solicite de la forma:

   fila = input(f"Ingrese fila {contadorFila}: ")

El usuario debera ingresar: ATGCGA
  
Las siguientes matrices podran utilizarse para comprobar si existe el codigo genico mutante o es simplemente de humano

    * MUTANTES:
    dna = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    dna = ["ATGCAA","CAGTGC","TTATAT","AGAACG","GTCCCC","TCACTG"]
    
    * HUMANOS:
    dna = ["ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"]
    dna = ["TTGCGA", "AAGTGC", "TTATTT", "AGATGG", "GCGTCA", "TCACTG"]

    
