#!/usr/bin/python3
rejected_ranges = list(range(101, 102)) + list(range(113, 114))
for i in range(97, 123):
    if i not in rejected_ranges:
        print("{}".format(chr(i)), end="")
