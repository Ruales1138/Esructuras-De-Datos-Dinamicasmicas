def mcd(a, b, idx = None):
    if idx == None:
        if a < b:
            idx = a
        if b < a:
            idx = b
    if a % idx == 0 and b % idx == 0:
        return idx
    else:
        return mcd(a, b, idx - 1)

print(mcd(48, 18))  # Output: 6
print(mcd(101, 103)) # Output: 1
print(mcd(22, 44))

