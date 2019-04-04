print("Type the binary you would like converted to decimal...")
#Original input
num = (input("> "))
#Converting number to a list of characters, then reversed it.
numl = str(num)[::-1]
#final decimal result
final = 0
#current power
power = 0
#list of digits
numlist = []

#list -> list
#takes in list of strings, and appends the corresponding integers to numlist.
#Then, it reverses the order.
def str2int(bin):
    global numlist
    global numl
    for i in numl:
        numlist.append(int(i))

#list -> number
#takes a list with the binary, and produces the corresponding decimal
def convert(number):
    global final
    global power
    if len(numlist) > 1:
        final = final + (int(numlist[0])*(2**power))
        power += 1
        convert(numlist.pop(0))
    elif len(numlist) == 1:
        final = final + (int(numlist[0])*(2**power))
        print(final)

convert(str2int(numl))
