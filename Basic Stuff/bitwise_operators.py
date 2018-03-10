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