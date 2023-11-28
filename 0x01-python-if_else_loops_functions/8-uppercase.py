#!/usr/bin/python3
def uppercase(s):
    for q in s:
        _upper = q if not ('a' <= q <= 'z') else chr(ord(q) - 32)
        print("{}".format(_upper), end="")
    print()
