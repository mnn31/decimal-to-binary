###############################################################
## Decimal to Binary
## Converts the inputted decimal number to binary
###############################################################

#CONSTANTS
NBITS = 10


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

    # No. of zeroes to be prepended
    n0 = NBITS - len(bits)
    str0 = '0' * n0  

    str1 = ''.join(bits)
    return (str0 + str1)


########################## MAIN PROGRAM ##########################
min1 = int(input("Enter a minimum decimal number: "))
max1 = int(input("Enter a maximum decimal number: "))
           
for dec in range(min1, max1+1):
    binary = dec2bin(dec)
    print(f'{dec} --> {binary}')
    
    
