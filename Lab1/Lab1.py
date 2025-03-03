m, n = list(map(int, input("Enter the dimensions m and n: ").split()))

def backyard(m, n):
    result = []
    array = []
    print("Enter the matrix elements: ")
    for _ in range(m):
        row = list(map(int, input().split()))
        array.append(row)

    for x in range(m):
        for y in range(n):
            if x % 2 == 0:
                result.append(array[x][y])
            else:
                result.append(array[x][n - 1 - y])
    
    return result

print(backyard(m, n))