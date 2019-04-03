#input, converted to string, and reversed
numl = str(input("> "))[::-1]
#final decimal result
final = 0
#current power
power = 0
#list of digits

numlist = []
#number -> list
#takes in a binary, and converts it to a list. Then, it flips the order.
def binlist(bin):
    global numlist
    global numl
    for digit in numl:
        numlist.append(int(digit))

#list -> number
#takes in a number in binary, and produces the corresponding decimal
def convert(number):
    global final
    global power
    if len(numlist) > 1:
        final = final + (int(numlist[0])*(2**power))
        power = power + 1
        convert(numlist.pop(0))
    elif len(numlist) == 1:
        final = final + (int(numlist[0])*(2**power))
        print(final)

convert(binlist(numl))
