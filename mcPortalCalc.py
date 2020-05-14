def askForDimension():
    dimensionInput = raw_input("What dimension do you have coords for? (Overworld [O]/Nether [N])  \n").upper()
    if dimensionInput == "O" or dimensionInput == "N":
        return dimensionInput

    print('Enter a valid dimension!')
    askForDimension()

def askForCoord(coord):
    coordInput = 0
    try:
        coordInput = int(raw_input('Enter ' + coord  + ' coordinate: \n'))
    except:
        print("Enter a valid coordinate!")
        askForCoord(coord)

    return coordInput

dimension = askForDimension()
x = askForCoord('X')
z = askForCoord('Z')

if dimension == 'O':
    #Do overworld calculation and return
    xNether = str(x / 8)
    zNether = str(z / 8)
    print('Nether coordinates are, X:' + xNether + ' Z:' + zNether)

#Do nether calculation and return
if dimension == 'N':
    xOverworld = str(x * 8)
    zOverworld = str(z * 8)
    print('Overworld coordinates are, X:' + xOverworld + ' Z:' + zOverworld)


