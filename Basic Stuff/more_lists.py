nums = [11, 12, 13, 14, 15]
print (min(nums))
print (max(nums))
print (sum(nums))
squares = [i**2 for i in range(1,51)]
print(squares)
print(squares[0:5])
print("First 10 Squares:")
for square in squares[:10]:
    print(square)
# Copy Lists
same_squares = squares[:]
print(same_squares)