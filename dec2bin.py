###############################################################
## Decimal to Binary
## Converts the inputted decimal number to binary
###############################################################


def dec2bin(dec):

    #collect each bit into a string called 'bits'
    if dec == 0:
        bits = ['0']
    else:
        bits = []

    while dec != 0:
        bit0 = dec % 2 #extract lsb (least significant bit)
        bits.insert(0, str(bit0)) #insert lsb at beginning of list
        dec = int(dec/2) #remove lsb

    str1 = ''.join(bits)
    return str1


########################## MAIN PROGRAM ##########################
min1 = int(input("Enter a minimum decimal number: "))
max1 = int(input("Enter a maximum decimal number: "))
           
for dec in range(min1, max1):
    binary = dec2bin(dec)
    print(f'{dec} --> {binary}')
    
    
