from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(path: List[int], sum_curr: int, curr: int):
            if curr >= len(candidates) or sum_curr + candidates[curr] > target:
                return
            elif sum_curr + candidates[curr] == target:
                paths.append(path + [candidates[curr]])
            else:
                helper(path + [candidates[curr]], sum_curr + candidates[curr], curr)
                helper(path, sum_curr, curr + 1)

        candidates.sort()
        paths = []
        helper([], 0, 0)
        return paths
