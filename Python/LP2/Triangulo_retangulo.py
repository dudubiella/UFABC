a = int(input(""))
b = int(input(""))
c = int(input(""))
if a < c:
    a, c = c, a
if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if not (a or b or c) > 0 or a > b + c:
    print("INVALIDO")
else:
    ret = "\nRETANGULO" if a ** 2 == b ** 2 + c ** 2 else ""
    print(f"VALIDO{ret}")