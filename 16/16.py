from math import prod
import fileinput

transmission = next(line.strip() for line in fileinput.input())
bits = ''.join(f'{int(hex, 16):04b}' for hex in transmission)

def process(bits, level=0):
    ver = int(bits[:3], 2)
    tid = int(bits[3:6], 2)
    rest = bits[6:]
    length = 6
    
    if tid == 4:
        num = ''
        len_ = 0
        for i in range(0, len(rest), 5):
            part = rest[i:i+5]
            num += part[1:]
            len_ += 5
            if part.startswith('0'):
                break
        val = int(num, 2)
        length += len_
        rest = rest[len_:]
    else:
        lid = rest[0]
        length += 1
        rest = rest[1:]
        if lid == '0':
            tot_length = int(rest[:15], 2)
            length += 15
            rest = rest[15:]
            len_ = 0
            vals = []
            while len_ < tot_length:
                rest, packet_len, ver_sum, val = process(rest, level+1)
                len_ += packet_len
                ver += ver_sum
                vals.append(val)
            length += len_
        elif lid == '1':
            packets = int(rest[:11], 2)
            length += 11
            rest = rest[11:]
            vals = []
            for _ in range(packets):
                rest, packet_len, ver_sum, val = process(rest, level+1)
                length += packet_len
                ver += ver_sum
                vals.append(val)
        match tid:
            case 0:
                val = sum(vals)
            case 1:
                val = prod(vals)
            case 2:
                val = min(vals)
            case 3:
                val = max(vals)
            case 5:
                val = 1 if vals[0] > vals[1] else 0
            case 6:
                val = 1 if vals[0] < vals[1] else 0
            case 7:
                val = 1 if vals[0] == vals[1] else 0
    return rest, length, ver, val

r, l, v, val = process(bits)
print(v)
print(val)