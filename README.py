p = 15
r = 12
print("Escribe 'p' o 'r':")
eleccion = input().strip().lower()

if eleccion == "p":
    print(f"El valor de p es: {p}")
elif eleccion == "r":
    print(f"El valor de r es: {r}")
else:
    print("Entrada no válida.")
