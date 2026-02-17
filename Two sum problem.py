#link for this leetcode problem : https://leetcode.com/problems/two-sum/
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target


def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i, num in enumerate(nums):
            ans= target - num
            if ans in hash_map:
                return[hash_map[ans],i]
            hash_map[num]=i
