alumnos = {
    "Juan": [8,9,7],
    "Ana": [10,9,8],
    "Luis": [6,7,8]
}

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")