x = input('Introduce un caracter: ')

asa = ord('a')
asz = ord('z')
asA = ord('A')
asZ = ord('Z')
asx = ord(x)

if asx >= asa and asx <= asz:
    print('La letra es minúscula')

elif asx >= asA and asx <= asZ:
    print('La letra es una mayúscula')

else: 
    print('No es una letra')