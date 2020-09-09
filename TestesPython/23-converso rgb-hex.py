def rgbhex():
    invalidmsg = "Inválido!!"
    red = int(input("Cor RED:"))
    if red < 0 or red > 255:
        return invalidmsg
    green = int(input("Cor Green:"))
    if green < 0 or green> 255:
        return invalidmsg
    blue = int(input("Cor BLUE:"))
    if blue < 0 or blue > 255:
        return invalidmsg
    val = (red << 16) + (green << 8) + blue
    result = hex(val)
    print(result[2:])

def hexrgb():
    hexval = input("Valor HEX:")
    if len(hexval) != 6:
        print("Invalido!")
        return
    else:
        hexval = int(hexval, 16)
    towhexdigiti = 2**8
    blue = hexval % towhexdigiti
    hexval = hexval >> 8
    green = hexval % towhexdigiti
    hexval = hexval >> 8
    red = hexval % towhexdigiti
    print(int(red),int(green),int(blue))

def convert():
    while True:
        option = input("Digite 1 para converter RGB em HEX. Digite 2 para converter HEX em RGB. Digite X para sair :")
        if option == "1":
            print("RGB para HEX..")
            rgbhex()
        elif option == "2":
            print("Hex para RGB..")
            hexrgb()
        elif option == "X" or "x":
            break
        else:
            print("Error")

convert()
