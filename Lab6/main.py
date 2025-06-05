class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = {}
        self.result = []


    def read_input(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                a, b = line.strip().split()
                self.add_neighbor(a, b)
                
        return self.graph


    def add_neighbor(self, a, b):
        if b not in self.graph:
            self.graph[b] = []
        if a not in self.graph:
            self.graph[a] = []
        self.graph[b].append(a)
        


    def topological_sort(self):
        self.visited = {vertex: False for vertex in self.graph}
        self.result = []

        for vertex in self.graph:
            if not self.visited[vertex]:
                self.DFS(vertex)

        self.result.reverse()
        return self.result


    def DFS(self, node):
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if not self.visited.get(neighbor, False):
                self.DFS(neighbor)
        self.result.append(node)
        


    def write_outed(self, filename, sorted_list):
        with open(filename, "w") as file:
            for node in sorted_list:
                file.write(node + "\n")


def main():
    graph = Graph()
    govern_in = "govern_in"
    govern_out = "govern_out"

    graph.read_input(govern_in)
    sorted_list = graph.topological_sort()
    graph.write_outed(govern_out, sorted_list)


if __name__ == "__main__":
    main()
