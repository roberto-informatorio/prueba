ventas1 = float(input("Por favor, ingrese el valor del dia 1: "))
ventas2 = float(input("Por favor, ingrese el valor del dia 2: "))


if ventas1 > ventas2:
    print("se vendio mas el dia 1:" + str(ventas1))
elif ventas2 > ventas1:
    print("se vendio mas el dia 2:" + str(ventas2))
else:
    print("las ventas son iguales: " + str(ventas1))