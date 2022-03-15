# def part1(transmission):
#     packet = hexToBinary(transmission)
#     packetVersion = int(packet[:3], 2)
#     typeID = int(packet[3:6], 2)
#     remaining = packet[6:]

#     if typeID == 4: 
#         num = [] 
#         while True:
#             if remaining[0] == '0':
#                 num.append(remaining[1:5])
#                 print(remaining)
#                 break
#             elif remaining[0] == '1':
#                 num.append(remaining[1:5])
#                 # num += remaining[1:5]
#                 remaining = remaining[5:len(remaining) - 1]
#                 print(remaining)
        

#     else:
#         num = []
#         if remaining[0] == '0':
#             remaining = remaining[1:len(remaining) - 1]
#             num.append(remaining[:15])
#         elif remaining[0] == '1'


#         ans = [str(binary) for binary in num]
#         ans = ''.join(ans)
#         print(int(ans, 2))
#     # else:
    
#     # if typeID == 4:

# def subpacket(subpacket):
#     packetVersion = int(subpacket[:3], 2)
#     typeID = int(subpacket[3:6], 2)
#     remaining = subpacket[6:]
#     num = [] 
#     while True:
#         if subpacket[0] == '0':
#             num.append(subpacket[1:5])
#             print(subpacket)
#             break
#         elif subpacket[0] == '1':
#             num.append(subpacket[1:5])
#             subpacket = subpacket[5:len(subpacket) - 1]
    
#     return packetVersion

def part1(transmission):
    packet = hexToBinary(transmission)
    packetVersion = int(packet[:3], 2)
    typeID = int(packet[3:6], 2)
    remaining = packet[6:]

    # check if literal
    if typeID == 4:

    # check if operator
    else:
        if remaining[0] == '0':
            lenSubpacket = int(remaining[1:15], 2)
            remaining = remaining[15:len(remaining) - 1]
        elif remaining[0] == '1':
            amountSubpacket = int(remaining[1:11], 2)
            remaining = remaining[11:len(remaining) - 1]
    
def verLen(remaining, length):
    sumVer = 0
    while length 
def amSub(remaining, amount):

def version(subpacket):
    subpacketVersion = int(subpacket[:3], 2) 
    while True:
        if subpacket[0] == '0':
            subpacket = subpacket[5:len(subpacket) - 1]
            break
        elif subpacket[0] == '1':
            subpacket = subpacket[5:len(subpacket) - 1]

    return subpacketVersion, subpacket

def hexToBinary(hex):
    return(bin(int(hex, 16)))[2:].zfill(4)


def main():
    with open('C:\dev\Advent of Code\Advent of Code 2021\Day 16\inputDay16.txt') as file:
        transmission = file.read().strip()

    part1(transmission)

if __name__ == '__main__':
    main()