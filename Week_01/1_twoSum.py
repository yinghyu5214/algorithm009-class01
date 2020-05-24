class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap.keys():
                j = hashmap[target - num]
                if i != j:
                    return [j, i]
            hashmap[num] = i # avoid same num in list: [3,3] 6

