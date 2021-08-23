def main():
    #escribe tu código abajo de esta línea
    pass

    saldoanterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el numero de cheques expendidos: "))
 
    saldofinal = ((saldoanterior + ingresos - egresos) - (cheques * 13)) * .925
    
    print("El saldo final de la cuenta es: " + str(saldofinal))


if __name__ == '__main__':
    main()
