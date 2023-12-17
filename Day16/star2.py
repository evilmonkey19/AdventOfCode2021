from dataclasses import dataclass
from numpy import prod


sampleData="880086C3E88112"

@dataclass
class Packet:
    version: int
    typeID: int
    literal: int
    length: int
    subpackets: list


def parse_packet(bits: str, depth: int = 0) -> Packet:
    version = int(bits[0:3], 2)
    typeID = int(bits[3:6], 2)
    position = 6

    # literal packet 
    if typeID == 4:
        literal, is_last = 0, False
        while not is_last:
            is_last = bits[position] == '0'
            literal = (literal << 4) | int(bits[position+1: position+5], 2)
            position += 5
        return Packet(version, typeID, literal, position, [])
    
    # operator packet
    length_typeID = int(bits[position], 2)
    position += 1

    if length_typeID == 0:
        subpackets= []
        total_length = int(bits[position: position+15], 2)
        position += 15
        length = 0
        while length != total_length:
            subpacket = parse_packet(bits[position: position + total_length - length], depth +1)
            subpackets.append(subpacket)
            length += subpacket.length
            position += subpacket.length
        return Packet(version, typeID, 0, position, subpackets)
    
    number_subpackets = int(bits[position: position+11],2)
    position += 11
    subpackets = []
    for _ in range(number_subpackets):
        subpacket = parse_packet(bits[position:], depth + 1)
        subpackets.append(subpacket)
        position += subpacket.length
    return Packet(version, typeID, 0, position, subpackets)

def compute(packet: Packet) -> int:
    if packet.typeID == 4:
        return packet.literal
    values = [compute(p) for p in packet.subpackets]
    if packet.typeID == 0:
        return sum(values)
    if packet.typeID == 1:
        return prod(values) # product
    if packet.typeID == 2:
        return min(values)
    if packet.typeID == 3:
        return max(values)
    if packet.typeID == 5:
        return int(values[0] > values[1])
    if packet.typeID == 6:
        return int(values[0] < values[1])
    if packet.typeID == 7:
        return int(values[0] == values[1])

# data = sampleData
data = open('data.txt', 'r', encoding="utf-8").read()

bits = bin(int(data, 16))[2:].zfill(len(data)*4)
packets = parse_packet(bits)

print(compute(packets))