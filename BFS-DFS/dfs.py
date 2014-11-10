"""
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
"""
def dfs(G, start):
    """Perform dfs on adjacency list of graph
    G: Adjacency list representation of graph.
    start: Index of start node.
    """
    visited = [False] * len(G)
    stack = []
    stack.append(start)
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            print(v)
            for neighbor in G[v]:
                stack.append(neighbor)

# This is your code. Takes O(V^2) because you are visiting every entry in
# the adjacency matrix, which has V^2 entries.
def dfs_adjacency_mat(G, start):
    visited=[False]*len(G[0])
    stack=[]
    stack.append(start)
    while len(stack)!=0:
        v=stack.pop()
        if visited[v]==False:
            visited[v]=True
            print(v)
            for w in range(len(G[0])):
                if G[v][w]!=0:
                    stack.append(w)

def main():
    # Represent graph as adjacency list, not adjacency matrix
    G = [[1],       # Node 0 (A) has node 1 (B) as neighbor
        [0, 6],    # Node 1 (B) has node 0 (A) and 6 (G) as neighbor
        [3],
        [2, 4, 6],
        [3, 5],
        [4, 6, 7],
        [1, 3, 5],
        [5]]
    print("Using adjacency list")
    dfs(G, 0)  # Start dfs at node 0 (i.e., node A)

    print('=' * 25)

    print("Using adjacency matrix")
    # Adjacency matrix
    graphx = [[1, 1, 0, 0, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 1, 0],
              [0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 1, 0],
              [0, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 1],
              [0, 1, 0, 1, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 1, 0, 1]]
    dfs_adjacency_mat(graphx, 0)


if __name__ == '__main__':
    main()