def producto(a, b):
    if b == 1:
        return a
    else:
        return a + producto(a, b=(b-1))

print(producto(3, 4))   # Output: 12
print(producto(5, 6))   # Output: 30