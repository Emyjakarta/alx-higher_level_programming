#!/usr/bin/python3
for q in range(ord('z'), ord('a') - 1, -1):
    if q % 2 == 0:
        _diff = 0
    else:
        _diff = 32
    print('{}'.format(chr(q - _diff)), end='')
