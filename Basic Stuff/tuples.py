# Tuples are immutable
min_max = (5,500)
print("Original Min & Max:")
for i in min_max:
    print(i)
min_max = (0, 1000)
print("Modified Min & Max:")
for i in min_max:
    print(i)
