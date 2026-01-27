def ConvertirBin(decimal):
    binario = ''

    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    return str(decimal) + binario
fich = open("decimal.txt", "r")
dec = fich.read()
fich.close()


binario = ConvertirBin(int(dec))


fich = open("binario.txt", "w")
fich.write(binario)
fich.close()