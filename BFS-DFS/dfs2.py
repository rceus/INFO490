# recursive DFS version
def dfs_rec(adjLists, visited, v):
    visited[v] = True
    print(v, " ", end='')
    for w in adjLists[v]:
        if(not visited[w]):
            dfs_rec(adjLists, visited, w)
 
             
# Usually dfs_rec() would be sufficient. However, if we don't want to pass
# a boolean array to our function, we can use another function dfs().
# We only have to pass the adjacency list and the source node to dfs(), 
#as opposed to dfs_rec(), where we have to pass the boolean array additionally.
def dfs(adjLists, s):
    visited = []
    n = len(adjLists)
    for i in range(n):
        visited.append(False)
    dfs_rec(adjLists, visited, s)
 
# ------------------------------------------------------------------
 
# create the graph in adjacency list representation
adjLists = [ [1,2,3], [5,6], [4], [2,4], [1], [], [4] ]
 
# test our implementation
dfs(adjLists, 0)

def dfs_iterative(adjLists, s):
    stack = []
    stack.append(s)
    n = len(adjLists)
    visited = []
    for i in range(0,n):
        visited.append(False)
         
    while(len(stack)>0):
        v = stack.pop()
        if(not visited[v]):
            visited[v] = True
            print(v, " ", end='')
 
            # auxiliary stack to visit neighbors in the order they appear
            # in the adjacency list
            # alternatively: iterate through the adjacency list in reverse order
            # but this is only to get the same output as the recursive dfs
            # otherwise, this would not be necessary
            stack_aux = []
            for w in adjLists[v]:
                if(not visited[w]):
                    stack_aux.append(w)
            while(len(stack_aux)>0):
                stack.append(stack_aux.pop())
                     
 
# ------------------------------------------------------------------
 
# create the graph in adjacency list representation
adjLists = [ [1,2,3], [5,6], [4], [2,4], [1], [], [4] ]
 
# test our implementation
dfs_iterative(adjLists, 0)
