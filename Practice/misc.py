n = 144
a = []
b = []
res = 0
total = 0

while n > 0:
    res = n % 2
    a.append(res)
    n = n // 2

a = a[::-1]  # Asegurar que `a` tiene los bits en el orden correcto
print(a)     # Representación binaria correcta

# Invertir los valores de 1 y 0 en `b`
for bit in a:
    b.append(1 if bit == 0 else 0)

print(b)  # Comprobamos el resultado de la inversión

# Convertir `b` de binario a decimal
total = sum(val * (2**i) for i, val in enumerate(reversed(b)))

print(total)  # ✅ Ahora total será el número correcto
