#Decimal to any Base:
def dtb(number, base):
    if number == 0:
        return str(0)
    else:
        box = number//base
        return dtb(box, base) + str(number%base)

#Any base to Decimal
def btd(number, base):
    start = 0
    end = 1
    pow = len(number)-1
    digit = 0
    while pow >= 0:
        bit = int(number[start:end])
        digit += bit*base**pow
        pow -= 1
        start += 1
        end += 1
    return digit

choice = 1
while choice != 2:
    print("Base Converter (2 to 10)")
    print("Number being converted")
    number = str(input("Number: "))
    base = int(input("Base: "))
    newnum = btd(number, base)

    print("Convert to")
    beys = int(input("Base: "))
    print("")
    ans = dtb(int(newnum), beys)

    print(f"Answer: {ans[1:]}")
    choice = int(input("Press 1 to convert another, Press 2 to exit: "))
    print("")