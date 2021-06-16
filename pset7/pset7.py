# Name:         San Varshney
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Problem Set VII
# Term:         Winter 2021

from typing import List


def to_adj_matrix(adj_list: List[List[int]]) -> List[List[int]]:
    """
    Given an adjacency list, return its equivalent adjacency matrix, in which
    each inner list represents a row in the matrix, with a 0 or 1 in the row
    indicating whether a directed edge does not or does exist, respectively,
    between the row vertex to the column vertex.

    >>> to_adj_matrix([[1, 2], [0, 2], [0, 1]])
    [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    """

    if len(adj_list) == 0:
        return []

    matrix = [[0 for x in range(len(adj_list))]
              for y in range(len(adj_list))]
    print(matrix)

    for i in range(len(adj_list)):
        for j in adj_list[i]:
            matrix[i][j] = 1

    print(matrix)
    return matrix


def to_adj_list(adj_matrix: List[List[int]]) -> List[List[int]]:
    """
    Given an adjacency matrix, return its equivalent adjacency list, in which
    each inner list represents all vertex labels for which the vertex at that
    index has a directed edge. For example, the first inner list contains all
    vertex labels for which Vertex 0 has a directed edge.

    >>> to_adj_list([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    [[1, 2], [0, 2], [0, 1]])
    """

    if len(adj_matrix) == 0:
        return []

    adjList = []

    for i in range(len(adj_matrix)):
        # print(str(adjList) + '  adjLIst')
        # print(str(i) + ' i')
        temp = []
        for j in range(len(adj_matrix[i])):
            # print(str(j) + ' j')
            if adj_matrix[i][j] == 1:
                temp.append(j)
        adjList.append(temp)
    return adjList


def order_bfs(adj_list: List[List[int]], start: int) -> List[int]:
    """
    Return a list of unique vertex labels from the given graph representing a
    breadth-first traversal of the graph starting at the specified vertex (with
    lower-numbered vertices chosen before higher-numbered vertices).

    >>> order_bfs([[1, 2], [0, 3], [0, 3], [1, 2]], 3)
    [3, 1, 2, 0]
    """

    queue_list = [start]
    result = [start]

    while len(queue_list) != 0:
        temp = queue_list.pop(0)
        for x in adj_list[temp]:
            if x not in result:
                result.append(x)
                queue_list.append(x)

    return result


def order_dfs(adj_list: List[List[int]], start: int,
              explored: List[int]) -> List[int]:
    """
    Return a list of unique vertex labels from the given adjacency list
    representing a depth-first traversal of the graph starting at the specified
    vertex (with lower-numbered vertices chosen over higher-numbered vertices).
    The explored argument may be used as an accumulator and will initially be
    an empty list.

    >>> order_dfs([[1, 2], [0, 3], [0, 3], [1, 2]], 2, [])
    [2, 0, 1, 3]
    """

    if start not in explored:
        explored.append(start)
        for i in adj_list[start]:
            order_dfs(adj_list, i, explored)
    return explored


def has_cycle(adj_list: List[List[int]], start: int, path: List[int]) -> bool:
    """
    Return True if the given graph (represented as an adjacency list) has a
    cycle and False otherwise. A graph has a cycle if there exists a path of
    unique edges that start and end at the same vertex.

    >>> has_cycle([[1, 2], [0, 3], [0, 3], [1, 2]], 0, [])  # square
    True
    >>> has_cycle([[1, 2], [], []], 0, [])  # tree
    False
    """

    dfs = order_dfs(adj_list, start, path)

    temp = dfs[len(dfs)-1]

    for _ in adj_list[temp]:
        if start in adj_list[temp]:
            return True
    return False


def count_components(adj_list: List[List[int]]) -> int:
    """
    Return the number of components in the given graph (represented as an
    adjacency list). A component is defined as a subgraph of vertices in which
    no vertex in the subgraph has a path (a sequence of edges) to a vertex
    outside the subgraph.

    >>> count_components([[1], [0], [3], [2], [5], [4]])
    3
    """

    temp = 0
    bfs = order_bfs(adj_list, temp)

    count = 1

    if len(adj_list) == len(bfs):
        return count
    # if not
    temp = len(bfs)

    while len(adj_list) > temp:
        bfs = order_bfs(adj_list, temp)
        count += 1
        temp += len(bfs)

    return count
