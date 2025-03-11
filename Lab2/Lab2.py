array = list(map(int, input("Enter array: ").split()))
P = int(input("Enter P: "))

def find_three_sum(array, P):
        for i in range(len(array)):
                value = set()  
                for j in range(i + 1, len(array)): 
                        num_3 = P - array[i] - array[j]
                        if num_3 in value:
                                return True
                        value.add(array[j])
        return False

print(find_three_sum(array, P))
