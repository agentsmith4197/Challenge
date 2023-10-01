def Pascals_triangle(n):
    triangle = [[1]]
    for a in range(1, n):
        number = [1]
        for i in range(1, len(triangle[-1])):
            middleNumber = triangle[-1][i - 1]
            mid = triangle[-1][i]
            newPascal = middleNumber + mid
            number.append( newPascal )
        number.append(1)
        triangle.append(number)
    return triangle

user = int(input("Enter the number for Pascal's Triangle: "))
if user > 0:
     pascals = Pascals_triangle(user)
    
     print(f"The Pascal's Triangle for {user} is:")
     for i in pascals:
        print(i)
else:
    print("Number of rows must be non-negative.")￼Enter
