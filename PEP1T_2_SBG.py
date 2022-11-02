print("\t\t\t\tPROGRAMA TELEGRAMA")
numelen = int(0)
numelen2 = int(0)
cadena = input("Teclea el mensaje: ")
print()
print("Cadena tecleada: ", cadena)
cadenamod = cadena[:-1]
cadenamod2 = cadenamod + " STOPSTOP"
cadenamod2 = cadenamod2.replace(".", " STOP")
print()
print("Mensaje a enviar: ", cadenamod2)
print()
frase = cadena.split()
for elem in frase:
    if len(elem) > 5:
        numelen = numelen + 1
    else:
        numelen2 = numelen2 + 1
precio = (0.50 * numelen) + (0.25 * numelen2)
print("La cadena contiene", len(frase), "palabras, de las cuales", numelen, "tienen más de 5 letras.")
print("Por tanto, al precio de 0.25€/palabra tenemos ", numelen2, "y a 0.50€/palabra hay otras", numelen, ".")
print(f"Total: {precio}€")


# Hola caracola patimi cocacola