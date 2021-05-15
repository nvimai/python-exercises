#========================

# Hexadecimal
# 0-9 a-f
# HEX 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
# DEC 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
# BIN 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111
#      0     1     2      3     4     5    6      7    8      9     10    11    12   13    14    15  
# 1 Byte = 2 hex
# 1 Byte (B) = 8 bits (b)
# 1 Kilo Byte (KB) = 1024 B
# 1 Giga Byte (GB) = 1024 KB
# 1 Tera Byte (TB) = 1024 GB

# 32 Mb = 4 MB
# 1000 Mb = 125 MB

# 1 Byte is from 0 to 255
# ff = 11111111 = 255
# 00000000, 00000001, ...., 1111 1111
# 00, 01, ff

# af << 2 => 1011 1100
# af >> 3 => 10101111 >> 3 =>00010101
# x = 0xaf >> 3
# print(f'{x:8b}')

#========================

# Finish 1 for $1, 2 for $5, 3 for $2
# 1. Finish the bitwise operators below:
# a. True AND False 
True & False = False

# b. True AND True

True & True = True

# c. False AND True
False & True = False

# d. False AND False

False & False = False

# e. True OR False

True | False = True
# f. True OR True
True | True = True
# g. False OR True
False | True = True
# h. False OR False
False | False = False
# i. True XOR False
True ^ False = True
# j. True XOR True
True ^ True = False
# k. False XOR True
False ^ True = True
# l. False XOR False
False ^ False = False

# 2. Finish the bitwise operators below:

# a. 34512 AND 23452

# 1000011011010000
# 0101101110011100
#&
# 0000001010010000

# 656

# b. 12352 AND 45722
# 1011100011
# 0001000111
#&
# 0001000011

# 12288

# c. 4598 AND 1235

# 1000111110110
# 0010011010011
#&
# 0000011010010

# 210

# d. 34512 OR 23452

# 1000011011010000
# 0101101110011100
#|
# 1101111111011100

# 57308

# e. 12352 OR 45722

# 1011100011
# 0001000111
#|
# 1011100111

# 45786

# f. 4598 OR 1235

# 1000111110110
# 0010011010011
#|
# 1010111110111

# 5623

# g. 34512 XOR 23452

# 1000011011010000
# 0101101110011100
# ^
# 1101110101001100

# 56652

# h. 12352 XOR 45722

# 1011100011
# 0001000111
# ^
# 1010100100

# 33498

# i. 4598 XOR 1235

# 1000111110110
# 0010011010011
# ^
# 1010100100101

# 5413


# k. DEX(12) << 2

# 1100
# 110000
#Answer is 110000 or 48

# l. DEX(24) << 4

# 11000
# 110000000
# answer is 110000000 or 384

# m. HEX(9d) << 3

# 10011101
# 10011101000
# answer is 0100 1110 1000 => 4e8

# n. HEX(ef) << 3

# 11101111
# 11101111000
# answer is 0111 0111 1000 = 778

# o. DEC(12) >> 2

# 1100
# 0011
# answer is 0011 or 3

# p. DEC(24) >> 4

# 11000
# 00001
# answer is 00001 or 1

# q. HEX(0c) >> 3

#1100
#0011
#answer is 0011 or 3

# r. HEX(ca) >> 3

# 11001010
# 00011001

#answer is 00011001 or HEX (19)



# 3. Colors - Convert from RGB to HEX or HEX to RGB
# a. RGB(234, 123, 9)

# 234
# 11101010
# ea

# 123
# 01111011
# 7b

# 9
# 00001001
# 09

#   # ea7b09


# b. RGB(0, 255, 255)

# 0
# 00000000
# 00

# 255
# 11111111
# ff

# 255
# 11111111
# ff

#  #00ffff


# c. #45afec

# 45
# 01000101
# 69

# af
# 10101111
# 175

# ec
# 11101100
# 236

#RGB(69, 175, 236)


# d. #0a88ab

# 0a
# 00001010
# 10

# 88
# 10001000
# 136

# ab
# 10101011
# 171

# RGB(10, 136, 171)k


# =====================
# Raspberry Pi: 
# 4. Using lesson 6 of Buzzer to write a program to indicate the KAYDEN in MORSE CODE