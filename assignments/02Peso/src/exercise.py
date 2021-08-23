def main():
    #escribe tu código abajo de esta línea
    pass

    pesoinicial = float(input("¿Cuanto pesas ahora?: "))
    pesofinal = float(input("¿Cuanto quieres pesar?: "))
    meses = int(input("Cuantos meses tienes para abajr de peso: "))
 
    kilos = (pesoinicial - pesofinal) / (meses)
    
    print("Debes bajar: " + str(kilos)  + "por mes")

if __name__ == '__main__':
    main()
