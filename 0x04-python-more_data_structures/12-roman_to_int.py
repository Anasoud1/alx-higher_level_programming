#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = 0
    i = 0
    while i < len(roman_string):
        if (i + 1) < len(roman_string):
            if roman_string[i] == "C" and roman_string[i + 1] == "D":
                s += 400
                i += 2
            elif roman_string[i] == "C" and roman_string[i + 1] == "M":
                s += 900
                i += 2
            elif roman_string[i] == "X" and roman_string[i + 1] == "L":
                s += 40
                i += 2
            elif roman_string[i] == "X" and roman_string[i + 1] == "C":
                s += 90
                i += 2
            elif roman_string[i] == "I" and roman_string[i + 1] == "V":
                s += 4
                i += 2
            elif roman_string[i] == "I" and roman_string[i + 1] == "X":
                s += 9
                i += 2
            else:
                s += rom[roman_string[i]]
                i += 1
        else:
            s += rom[roman_string[i]]
            i += 1
    return s
