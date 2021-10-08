#!/bin/env python3

def bin2dec():
    '''Convert binary to decimal'''
    numbers = input("Enter the binary to convert to ascii:\n")
    binary = numbers.split()
    nums_list = []
    for octet in binary:
        power = len(octet) - 1
        decimal = 0
        for number in octet:
            decimal += int(number) * ( 2 ** int(power) )
            power -= 1
        nums_list.append(decimal)
    return nums_list


def dec2ascii():
    '''Convert decimal to ascii'''
    decimal_list = bin2dec()
    ascii_list = []
    for number in decimal_list:
        ascii_list.append(chr(number))
    return ascii_list


def convert():
    '''Convert list of ascii characters to string'''
    ascii_list = dec2ascii()
    string = ""
    for elem in ascii_list:
        string += elem
    return string

print(f"\nDecoded text:\n{convert()}")
