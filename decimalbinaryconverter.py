#DecimalToBinaryConverter

#Binary Number: has only 1s and 0s
#Rightmost bit (binary digit) is 2^0, and the power raises for every digit, just like in decimal system

#How Binary Works:
#Example (Least Significant Bit to Most Significant Bit):
#110001010
#0x2^0 + 1x2^1 + 0x2^2 + 1x2^3 + 0x2^4 + 0x2^5 + 0x2^6 + 1x2^7 + 1x2^8 = 2 + 8 + 128 + 256 = 394

#Decimal to Binary: Divide the number to two. Take note of the remainder for each. Keep going until answer becomes zero. (Most Significant Bit to Least Significant Bit)
#Example:
#394/2 = 197r0; 197/2 = 98r1; 98/2 = 49r0; 49/2 = 24r1; 24/2 = 12r0; 12/2 = 6r0; 6/2 = 3r0; 3/2 = 1r1; 1/2 = 0r1

def dtb(d):
    if d == 0:
        return str(0)
    else:
        return dtb(d//2) + str(d%2)

def btd(b):
    if ("2" in b) or ("3" in b) or ("4" in b) or ("5" in b) or ("6" in b) or ("7" in b) or ("8" in b) or ("9" in b): 
        return "none. Value must be binary only."
    elif ("1" in b) or ("0" in b):
        start = 0
        end = 1
        pow = len(b)-1
        digit = 0
        while pow >= 0:
            bit = int(b[start:end])
            digit += bit*2**pow
            pow -= 1
            start += 1
            end += 1
        return digit

choice = 0
while choice != 3:
    print("Decimal and Binary Converter\n1. Decimal to Binary\n2. Binary to Decimal\n3. Exit")
    choice = int(input("Input: "))
    if choice == 1:
        digit = int(input("Please input a number: "))
        resp = str(dtb(digit)[1:])
        print(f"The binary equivalent of {digit} is {resp}\n")
    elif choice == 2:
        binary = input("Please input a binary number: ")
        resp = btd(str(binary))
        print(f"The decimal equivalent of {binary} is {resp}\n")
