###############################################################
## Decimal to Binary
## Converts the inputted decimal number to binary
###############################################################

def dec2bin(dec):
    bits = []

    bit0 = dec % 2
    bits.insert(0, bit0)
    dec = int(dec/2)
    bit1 = dec % 2
    bits.insert(0, bit1)
    dec = int(dec/2)
    bit2 = dec % 2
    bits.insert(0, bit2)

    return bits
    

#dec = int(input('Enter a decimal number: '))
for dec in range(20):
    binary = dec2bin(dec)
    print(f'{dec} --> {binary}')
    
    
