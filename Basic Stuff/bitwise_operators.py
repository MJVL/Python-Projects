print(0b1),
print(0b10),
print(0b11 * 0b11)

print(bin(10)),
print(hex(10)),
print(oct(10))

for i in range(2,6):
	print(bin(i))

shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))


print(bin(0b1110 & 0b101))
print(bin(0b1110 | 0b101))
print(bin(0b1110 ^ 0b101))
print(bin(~0b110))

# Check if bit is on at position 4
def check_bit4(input):
	mask = 0b1000
	desired = input & mask
	if desired > 0:
		return "on"
	else:
		return "off"


print(check_bit4(0b1))
print(check_bit4(0b11011))
print(check_bit4(0b1010))

# Turn bit on at third position
a = 0b10111011
mask = 0b100
print(bin(a | mask))

# Flip all bits in a
a = 0b11101110
mask = 0b11111111
print(bin(a ^ mask))

# Flip nth bit
def flip_bit(number, n):
	return bin(number ^ ob1 << (n-1))
