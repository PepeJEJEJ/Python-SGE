def ConvertirBin(decimal):
    binario = ""
    # mientras la división entera del decimal entre 2 no sea cero
    while decimal != 0:
        # concatena el resto de dividirlo entre 2 al resultado por la izquierda
        binario = str(decimal % 2) + binario
        # volcar en el decimal el resultado de la división entera entre 2
        decimal = decimal // 2
    return binario
