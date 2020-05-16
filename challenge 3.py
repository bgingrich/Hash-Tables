# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# 4 + -1 + 9 + -56 + 201 + 18 = 175

Array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

smallSum = 0

for i in Array:
    smallSum += min(i)

print (smallSum)