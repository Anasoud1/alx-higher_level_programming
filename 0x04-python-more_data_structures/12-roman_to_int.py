#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
           "VIII": 8, "XI": 9, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = 0
    for i in roman_string:
        s += rom[i]
    return s
