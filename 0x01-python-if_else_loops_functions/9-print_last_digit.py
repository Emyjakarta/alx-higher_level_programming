#!/usr/bin/python3
def print_last_digit(number):
    _last_digit = abs(number) % 10
    print(_last_digit, end="")
    return _last_digit
