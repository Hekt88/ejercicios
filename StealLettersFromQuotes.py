#CREA UN PROGRAMA QUE TRAS INTRODUCIR EL USER UNA FRASE, DESPUES LE PREGUNTA QUE LETRA QUIERE ELIMINAR DE LA FRASE, Y TRAS INTRODUCIRLA MUESTRA LA FRASE SIN ESA LETRA

frase=input("Introduce una frase que te guste:   ")

letra_delete=input("que letra quieres eliminar de la frase??    ")



frase_modificada=frase.replace(letra_delete, "#")

print(frase_modificada)