from Lab4 import PriorityQueue

def main():
    pq = PriorityQueue()

    while True:
        command = input("Input command (add, max_value, peek, check, exit): ").split()

        if command[0] == "add":
            try:
                value = command[1]
                priority = int(command[2])
                pq.insert(value, priority)
            except (IndexError, ValueError):
                print("Enter value and priority(add {value priority})")
        elif command[0] == "max_value":
            print(pq.extract_max())
        elif command[0] == "peek":
            print(pq.peek())
        elif command[0] == "check":
            pq.display()
        elif command[0] == "exit":
            print("Goodbye")
            break
        else:
            print("Use the right commands")

if __name__ == '__main__':
    main()
    