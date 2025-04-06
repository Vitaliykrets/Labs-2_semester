class Node:
    def __init__(self, value, priority):
        self.value = value 
        self.priority = priority 
    
    def __repr__(self):
        return f"Value: {self.value}, Priority: {self.priority}"


class PriorityQueue:
    def __init__(self):
        self.heap = [] 
        
    def insert(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def extract_max(self):
        if not self.heap:
            return "The queue is empty"
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def peek(self):
        return self.heap[0] if self.heap else "The queue is empty"

    def display(self):
        print("A queue with priorities:", self.heap)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(50, 2)
    pq.insert(30, 5)
    pq.insert(40, 1)
    pq.insert(2, 4)
    pq.display()
    print("The highest priority: ", pq.extract_max())
    pq.display()
