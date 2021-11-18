# Given an alphabetically sorted list of words in a foreign, yet-to-be
# discovered alphabet, determine the order of the alphabet. The list of words
# contains all characters of the alphabet.
# O(n+m) runtime
# Ex: "d", "ro", "ri", "or" -> "droi"
# Assumption: input is valid

from typing import List, Dict
from queue import Queue


def top_sort_kahns(graph: Dict[str, str]) -> str:
    ordering = ''
    queue = Queue()
    in_degree = {k:0 for k in graph}
    for v in graph.values():
        for node in v:
            in_degree[node] += 1

    for k, v in in_degree.items():
        if v == 0:
            queue.put(k)

    while not queue.empty():
        c = queue.get()
        ordering += c
        out_nodes = graph[c]
        for node in out_nodes:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                queue.put(node)

    return ordering

def top_sort_dfs(graph: Dict[str, str]) -> str:
    visited: Dict[str, str] = {}

    def dfs (root: str, graph: Dict[str, str]) -> str:
        ordering = ''
        if root not in visited:
            visited[root] = True
            for nodes in graph[root]:
                for node in nodes:
                    ordering += dfs(node, graph)
            ordering += root
        return ordering

    reverse_order = ''
    for c in graph:
        reverse_order += dfs(c, graph)

    return reverse_order[::-1]


def solution(words: List[str]) -> str:
    alpha_map = {}
    for word in words:
        for c in word:
            alpha_map[c] = []

    for i in range(1, len(words)):
        prev = words[i - 1]
        curr = words[i]
        for j in range(min(len(prev), len(curr))):
            if prev[j] != curr[j]:
                alpha_map[prev[j]].append(curr[j])
                break

    return top_sort_dfs(alpha_map)
    # return top_sort_kahns(alpha_map)


print(solution(['wrt','wrf','er','ett','rftt'])) # wertf
print(solution(['baa', 'abcd', 'abca', 'cab', 'cad'])) # bdac
print(solution(['caa', 'aaa', 'aab'])) # cab
