file = open("misc files/output.txt", "r")
print(file.read())
file.close()

file = open("misc files/output.txt", "r")
print(file.readline())
print(file.readline())
file.close()

list_bin = []
with open("misc files/output.txt", "r") as file:
	for line in file:
		list_bin.append(line.rstrip())

print list_bin

