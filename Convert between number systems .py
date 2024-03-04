#Convert between number systems 
#DECIMAL TO BINARY FUNCTION
def decimal_to_binary(decimal_num):
    binary_num = ""
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = decimal_num // 2
    return binary_num
#BINARY TO DECIMAL FUNCTION
def binary_to_decimal(binary):
    decimal = 0
    counter = 0
    while binary > 0:
        remainder = binary % 10
        num = remainder*(2**counter)
        decimal = decimal+num
        binary = binary//10
        counter += 1
    return decimal
#DECIMAL TO HEX FUNCTION
def decimal_to_hexadecimal(decimal_num):
    hex_digits = "0123456789ABCDEF"
    hexadecimal_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_num = hex_digits[remainder] + hexadecimal_num
        decimal_num = decimal_num // 16
    return hexadecimal_num
#HEX TO DECIMAL FUNCTION
def hexadecimal_to_decimal(hexadecimal):
    hex_digits = '0123456789ABCDEF'
    decimal_num = 0
    power = len(hexadecimal) - 1
    for digit in hexadecimal:
        decimal_num += hex_digits.index(digit) * (16 ** power)
        power -= 1
    return decimal_num
#DECIMAL TO OCTAL FUNCTION
def decimal_to_octal(decimal_num):
    octal_num = ""
    while decimal_num > 0:
        octal_num = str(decimal_num % 8) + octal_num
        decimal_num = decimal_num // 8
    return octal_num
#OCTAL TO DECIMAL FUNCTION
def octal_to_decimal(octal):
    decimal_num = 0
    power = 0
    while octal != 0:
        decimal_num += (octal % 10) * (8 ** power)
        octal //= 10
        power += 1
    return decimal_num                           

while True: 
    #menu 1             
    print('''numbering system converter:
    a Insert new numbers
    b Exit''' )                                     
    choose1 = input("what is your choice?...")
    
    if choose1=="b"or choose1=="B"or choose1=="Exit":
        print("exiting the program")
        break
    #MENU 2
    elif choose1=="a"or choose1=="A"or choose1=="Insert new numbers":  
        print('''Choose from which system you want to convert:  
        1 Decimal
        2 Binary
        3 octal
        4 hexadecimal''')                          
        choose2 = input("what is your choice?...")
        #MENU 3
        print(''' Please select the system you want to convert to:
        1 Decimal
        2 Binary
        3 octal
        4 hexadecimal''')                               
        choose3=input("what is your choice?...")
        #BINARY TO DECIMAL
        if choose2 == ("2" or "Binary") and choose3 == ("1" or "Decimal"): 
            binary = int(input("please enter a binary number with[o,1]only: "))
            decimal=binary_to_decimal(binary)
            print(decimal)
        #BINARY TO OCTAL
        elif choose2 == ("2" or "Binary") and choose3 == ("3" or "octal"):
            binary = int(input("please enter a binary number with[o,1]only: "))
            result1 = decimal_to_octal(binary_to_decimal(binary))
            print( result1 )
        #BINARY TO HEX
        elif choose2 == ("2" or "Binary") and choose3 == ("4" or "hexadecimal"):
            binary = int(input("please enter a binary number with[o,1]only: "))
            result2 = decimal_to_hexadecimal(binary_to_decimal(binary))
            print(result2)
        #DECIMAL TO BINARY 
        elif choose2 == ("1" or "Decimal") and choose3 == ("2" or "Binary"):
            decimal = int(input("enter a decimal number: "))
            print(decimal_to_binary(decimal))
        #DECIMAL TO OCTAL
        elif choose2 == ("1" or "Decimal") and choose3 == ("3" or "octal"):
            decimal = int(input("enter a decimal number: "))
            print(decimal_to_octal(decimal))
        #DECIMAL TO HEX
        elif choose2 == ("1" or "Decimal") and choose3 == ("4" or "hexadecimal"):
            decimal = int(input("enter a decimal number: "))
            print(decimal_to_hexadecimal(decimal))
        #HEX TO DECIMAL
        elif choose2 == ("4" or "hexadecimal") and choose3 == ("1" or "Decimal"):
            hexadecimal = str(input("enter a hexadecimal number: "))
            print(hexadecimal_to_decimal(hexadecimal))
        #HEX TO BINARY
        elif choose2 == ("4" or "hexadecimal") and choose3 == ("2" or "Binary"):
            hexadecimal = str(input("enter a hexadecimal number: "))
            result3 = decimal_to_binary(hexadecimal_to_decimal(hexadecimal))
            print(result3)
        #HEX TO OCTAL
        elif choose2 == ("4" or "hexadecimal") and choose3 == ("3" or "octal"):
            hexadecimal = str(input("enter a hexadecimal number: "))
            result4 = decimal_to_octal(hexadecimal_to_decimal(hexadecimal))
            print(result4)
        #OCTAL TO DECIMAL
        elif choose2== ("3" or "octal") and choose3 == ("1" or "Decimal"):
            octal = int(input("enter an octal number: "))
            print(octal_to_decimal(octal))
        #OCTAL TO BINARY
        elif choose2 == ("3" or "octal") and choose3 == ("2" or "Binary"):
            octal = int(input("enter a octal number: "))
            result5 = decimal_to_binary(octal_to_decimal(octal))
            print(result5)
        #OCTAL TO HEX
        elif choose2 == ("3" or "octal") and choose3 == ("4" or "hexadecimal"):
            octal = int(input("enter a octal number: "))
            result6 = decimal_to_hexadecimal(octal_to_decimal(octal))
            print(result6)
        
        else: 
            print("not a valid choice")                                  
        continue        
    else :
        print("not a valid choice")                                  
    continue    
#IF You want to Try the program let:
#HEX=1AC          | BINARY=101110 | OCTAL=33       | DECIMAL=12
#EXPECTED OUTPUT:      
#in dec=428       | in dec=46     | in Dec=27      | in bin=1100
#in bin=110101100 | in oct=56     | in bin=1110111 | in oct=14
#in oct=654       | in hex=2e     | in hex=1B      | in hex=C 