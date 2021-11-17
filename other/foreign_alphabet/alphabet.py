# Given an alphabetically sorted list of words in a foreign, yet-to-be
# discovered alphabet, determine the order of the alphabet. The list of words
# contains all characters of the alphabet.
# O(n+m) runtime
# Ex: "d", "ro", "ri", "or" -> "droi"

def longest_path(root: str, graph: dict[str, list[str]]) -> str:
    path = root
    if graph[root] == []:
        return path
    for node in graph[root]:
        some_path = path + longest_path(node, graph)
        if path < some_path:
            path = some_path
    return path

def solution(words: list[str]) -> str:
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

    potential_roots = []

    # find the root
    for key in alpha_map.keys():
        potential_roots.append(key)

    for val in alpha_map.values():
        for letter in val:
            if letter in potential_roots:
                potential_roots.remove(letter)

    # find longest path from root
    return longest_path(potential_roots[0], alpha_map)

print(solution(['wrt','wrf','er','ett','rftt'])) # wertf
