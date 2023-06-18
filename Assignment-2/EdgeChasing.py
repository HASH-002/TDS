class Graph:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.edges = [[] for _ in range(num_processes)]
    
    def add_edge(self, process_id, edge):
        self.edges[process_id].append(edge)
    
    def detect_deadlocks(self):
        for process_id in range(self.num_processes):
            visited = set()
            stack = [process_id]
            while stack:
                current_process = stack.pop()
                visited.add(current_process)
                for edge in self.edges[current_process]:
                    next_process = edge[1]
                    if next_process == process_id:
                        print(f"Deadlock detected involving process {process_id}")
                        return
                    elif next_process not in visited:
                        stack.append(next_process)
        print("No deadlocks detected")

# Example 1
'''
graph = Graph(6)
graph.add_edge(0, (0, 1))
graph.add_edge(1, (1, 4))
graph.add_edge(2, (2, 4))
graph.add_edge(3, (3, 0))
graph.add_edge(4, (4, 3))
graph.add_edge(5, (5, 1))
graph.detect_deadlocks()
'''
#Example 2
# '''
graph = Graph(10)
graph.add_edge(0, (0, 1))
graph.add_edge(0, (0, 2))
graph.add_edge(1, (1, 3))
graph.add_edge(2, (2, 4))
graph.add_edge(3, (3, 4))
graph.add_edge(4, (4, 5))
graph.add_edge(4, (4, 6))
graph.add_edge(6, (6, 7))
graph.add_edge(7, (7, 8))
graph.add_edge(8, (8, 9))
graph.detect_deadlocks()
# '''