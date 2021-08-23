def main():
    #escribe tu código abajo de esta línea
    pass
    cal1 = float(input("Dame la primera calificacion: "))
    cal2 = float(input("Dame la segunda calificacion: "))
    cal3 = float(input("Dame la tercera calificacion: "))
    cal4 = float(input("Dame la cuarta calificacion: "))

    promedio = (cal1 + cal2 + cal3 + cal4) / 4
    
    print("El promedio es: " + str(promedio))

if __name__ == '__main__':
    main()
