array = list(map(int, (input("Enter N: ").split())))
P = int(input("Enetr P: "))

def find_three_sum(array, P):
        
        for num_1 in range(len(array)):
                value = list()
                for num_2 in range(num_1 + 1, len(array)):
                        num_3 = P - array[num_1] - array[num_2]
                        if num_3 in value and num_3 != array[num_1] and num_3 != array[num_2]:
                                return True
                        value.append(array[num_2]) 
        
        return False        
        
print(find_three_sum(array, P))
