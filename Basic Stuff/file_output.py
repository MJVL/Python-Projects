my_list = [bin(i ** 2) for i in range(1, 11)]

file = open("misc files/output.txt", "w")

for item in my_list:
	file.write(str(item) + "\n")

file.close()

with open("misc files/output.txt", "w") as textfile:
	textfile.write("This worked!")

print textfile.closed