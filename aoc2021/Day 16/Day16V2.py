# from re import I


# class Bitstream:
#     def __init__(self, file):
#         transmission = file.read()
#         binary = bytes.fromhex(transmission)

#         self.pos = 0
#         self.bits = ''

#         self.bits = ''.join(map('{:08b}'.format, binary))

#     def binaryToInt(self, nbits):
#         ans = int(self.bits[self.pos:self.pos + nbits], 2)
#         self.pos += nbits
#         return ans

#     def decodePacket(self):
#         version = self.binaryToInt(3)
#         typeID = self.binaryToInt(3)
#         data = self.decodePacketData(typeID)
#         return (version, typeID, data)

#     def decodeValueData(self):
#         value = 0
#         group = 0b10000

#         while group and 0b10000:
#             group = self.binaryToInt(5)
#             value <<= 4
#             value += group and 0b10000
        
#         return value

#     def decodeNPackets(self, n):
#         return[self.decodePacket() for _ in range(n)]

#     def decodeLengthPackets(self, length):
#         end = self.pos + length
#         packets = []

#         while self.pos < end:
#             packets.append(self.decodePacket())

#         return packets

#     def decodeOperatorData(self):
#         length = self.binaryToInt(1)

#         if length == 1:
#             return self.decodeNPackets(self.binaryToInt(11))
#         return self.decodeLengthPackets(self.binaryToInt(15))
    
#     def decodePacketData(self, typeID):
#         if typeID == 4:
#             return self.decodeValueData()
#         return self.decodeOperatorData()

# def sumVersions(transmission):
#     version, typeID, data = transmission

#     if typeID == 4:
#         return version

#     return version + sum(map(sumVersions, data))

# file = open('C:\dev\Advent of Code\Advent of Code 2021\Day 16\inputDay16.txt')

# stream = Bitstream(file)
# packet = stream.decodePacket()
# sum = sumVersions(packet)

# print(sum)

from math import prod

class Bitstream:
	def __init__(self, file):
		rawdata = bytes.fromhex(file.read())
		self.bits = ''.join(map('{:08b}'.format, rawdata))
		self.pos = 0

	def decode_int(self, nbits):
		res = int(self.bits[self.pos:self.pos + nbits], 2)
		self.pos += nbits
		return res

	def decode_n_packets(self, n):
		return [self.decode_one_packet() for _ in range(n)]

	def decode_len_packets(self, length):
		end = self.pos + length
		pkts = []

		while self.pos < end:
			pkts.append(self.decode_one_packet())

		return pkts

	def decode_value_data(self):
		value = 0
		group = 0b10000

		while group & 0b10000:
			group = self.decode_int(5)
			value = (value << 4) + (group & 0b1111)

		return value

	def decode_operator_data(self):
		if self.decode_int(1):
			return self.decode_n_packets(self.decode_int(11))
		return self.decode_len_packets(self.decode_int(15))

	def decode_packet_data(self, tid):
		if tid == 4:
			return self.decode_value_data()
		return self.decode_operator_data()

	def decode_one_packet(self):
		version = self.decode_int(3)
		tid     = self.decode_int(3)
		data    = self.decode_packet_data(tid)
		return (version, tid, data)

def sum_versions(packet):
	v, tid, data = packet
	return v if tid == 4 else v + sum(map(sum_versions, data))

def evaluate(packet):
	_, tid, data = packet

	if tid == 4:
		return data

	values = map(evaluate, data)

	if tid == 0: return sum(values)
	if tid == 1: return prod(values)
	if tid == 2: return min(values)
	if tid == 3: return max(values)

	a, b = values

	if tid == 5: return int(a > b)
	if tid == 6: return int(a < b)
	if tid == 7: return int(a == b)

	raise NotImplementedError('Unimplemented tid={}'.format(tid))


fin = open('C:\dev\Advent of Code\Advent of Code 2021\Day 16\inputDay16.txt')

stream = Bitstream(fin)
packet = stream.decode_one_packet()
vsum   = sum_versions(packet)
result = evaluate(packet)

print(vsum, result)