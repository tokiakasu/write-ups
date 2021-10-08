## Leviathan 4-5
Category: `binary`

## Description
There is no information for this level, intentionally.

## Analysis
```
leviathan4@leviathan:~$ ls -al
total 24
drwxr-xr-x  3 root root       4096 Aug 26  2019 .
drwxr-xr-x 10 root root       4096 Aug 26  2019 ..
-rw-r--r--  1 root root        220 May 15  2017 .bash_logout
-rw-r--r--  1 root root       3526 May 15  2017 .bashrc
-rw-r--r--  1 root root        675 May 15  2017 .profile
dr-xr-x---  2 root leviathan4 4096 Aug 26  2019 .trash
leviathan4@leviathan:~$ ls -la .trash/
total 16
dr-xr-x--- 2 root       leviathan4 4096 Aug 26  2019 .
drwxr-xr-x 3 root       root       4096 Aug 26  2019 ..
-r-sr-x--- 1 leviathan5 leviathan4 7352 Aug 26  2019 bin
leviathan4@leviathan:~$ ./.trash/bin 
01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010 
```
We have binary that outputs binary, and it would be too easy to just put these numbers into something like "convert binary to ascii".
> Binary to ascii converter - onlineasciitools.com/convert-binary-to-ascii

So I converted the first octet on paper myself
> How to Convert Binary to Decimal - youtu.be/a2FpnU9Mm3E

and then wrote a simple Python script to convert any binary code
```
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
```
It's time to convert our binary code
```
curvtd@github:~/write-ups$ ./bin2ascii.py
Enter the binary to convert to ascii:
01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010 

Decoded text:
Tith4cokei
```
NOW I can accept my solution

