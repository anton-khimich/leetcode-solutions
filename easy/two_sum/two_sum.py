from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    d = {}
    ret = []
    for i, j in enumerate(nums):
        d[i] = j
    for i in nums:
        if target - i in nums:
            try:
                ret.append(nums.index(target - i, nums.index(i) + 1))
                ret.append(nums.index(i))
            except ValueError:
                continue
            break
    return ret

def main():
    i = [int(i) for i in input().split()]
    nums = i[0: -1]
    target = i[-1]
    print(two_sum(nums, target))

if __name__ == '__main__':
    main()
