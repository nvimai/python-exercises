#========================

# Hexadecimal
# 0-9 a-f
# HEX 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f
# DEC 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
# BIN 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111

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
# b. True AND True
# c. False AND True
# d. False AND False
# e. True OR False
# f. True OR True
# g. False OR True
# h. False OR False
# i. True XOR False
# j. True XOR True
# k. False XOR True
# l. False XOR False

# 2. Finish the bitwise operators below:
# a. 34512 AND 23452
# b. 12352 AND 45722
# c. 4598 AND 1235
# d. 34512 OR 23452
# e. 12352 OR 45722
# f. 4598 OR 1235
# g. 34512 XOR 23452
# h. 12352 XOR 45722
# i. 4598 XOR 1235
# k. DEX(12) << 2
# l. DEX(24) << 4
# m. HEX(9d) << 3
# n. HEX(ef) << 3
# o. DEC(12) >> 2
# p. DEC(24) >> 4
# q. HEX(0c) >> 3
# r. HEX(ca) >> 3

# 3. Colors - Convert from RGB to HEX or HEX to RGB
# a. RGB(234, 123, 9)
# b. RGB(0, 255, 255)
# c. #45afec
# d. #0a88ab