renta = float(input("Cual es tu renta "))
if renta < 10000:
    inpuesto = renta * 0.05
    print(f"Inpuestos a pagar {inpuesto}")
elif renta >= 10000 and renta <= 20000:
    inpuesto = renta * 0.15
    print(f"Inpuestos a pagar {inpuesto}")

elif renta >= 20000 and renta <= 35000:
    inpuesto = renta * 0.2
    print(f"Inpuestos a pagar {inpuesto}")

elif renta >= 35000 and renta <= 60000:
    inpuesto = renta * 0.3
    print(f"Inpuestos a pagar {inpuesto}")

elif renta > 60000:
    inpuesto = renta * 0.45
    print(f"Inpuestos a pagar {inpuesto}")