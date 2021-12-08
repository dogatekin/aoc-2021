import fileinput
from collections import defaultdict


lines = [line.strip() for line in fileinput.input()]

part1 = 0
part2 = 0
for line in lines:
    inps, outs = line.split(' | ')
    inps = inps.split()
    outs = outs.split()
    part1 += sum(len(out) in (2, 3, 4, 7) for out in outs)

    possibilities = {signal: set(range(7)) for signal in 'abcdefg'}
    signals = {}
    for inp in inps:
        if len(inp) == 2:
            signals[1] = set(inp)
        elif len(inp) == 3:
            signals[7] = set(inp)
        elif len(inp) == 4:
            signals[4] = set(inp)
        elif len(inp) == 7:
            signals[8] = set(inp)
                
    top = (signals[7] - signals[1]).pop()
    nine_parts = signals[4].union({top})
    
    for inp in inps:
        if all(part in inp for part in nine_parts) and len(inp) == 6:
            signals[9] = set(inp)
    
    bottom = (signals[9] - nine_parts).pop()
    bottom_left = (signals[8] - signals[9]).pop()
    
    zero_parts = signals[1].union({top, bottom, bottom_left})
    for inp in inps:
        if all(part in inp for part in zero_parts) and len(inp) == 6:
            signals[0] = set(inp)
            
    top_left = (signals[0] - zero_parts).pop()
    middle = (signals[8] - signals[0]).pop()
    
    two_parts = {top, middle, bottom, bottom_left}
    for inp in inps:
        if all(part in inp for part in two_parts) and len(inp) == 5:
            signals[2] = set(inp)
    
    top_right = (signals[2] - two_parts).pop()
    bottom_right = (signals[1] - {top_right}).pop()
    
    digits = {
        ''.join(sorted({top, top_left, top_right, bottom_left, bottom_right, bottom})): '0',
        ''.join(sorted({top_right, bottom_right})): '1',
        ''.join(sorted({top, top_right, middle, bottom_left, bottom})): '2',
        ''.join(sorted({top, top_right, middle, bottom_right, bottom})): '3',
        ''.join(sorted({top_right, middle, top_left, bottom_right})): '4',
        ''.join(sorted({top, top_left, middle, bottom_right, bottom})): '5',
        ''.join(sorted({top, top_left, middle, bottom_right, bottom, bottom_left})): '6',
        ''.join(sorted({top_right, bottom_right, top})): '7',
        ''.join(sorted({top, top_right, top_left, middle, bottom_left, bottom_right, bottom})): '8',
        ''.join(sorted({top, top_right, top_left, middle, bottom_right, bottom})): '9'
    }
    
    part2 += int(''.join(digits[''.join(sorted(out))] for out in outs))
        
print(part1)
print(part2)