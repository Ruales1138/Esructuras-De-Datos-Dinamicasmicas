def es_palindromo(cadena):
       if len(cadena) == 1:
              return True
       if cadena[0] == cadena[-1]:
              return es_palindromo(cadena[0:3])
       # return cadena[0:2]

print(es_palindromo("radar"))     # Output: True
print(es_palindromo("reconocer")) # Output: True
print(es_palindromo("python"))    # Output: False

n = "p"
print(len(n))