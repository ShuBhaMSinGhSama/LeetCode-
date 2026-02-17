#https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
# Its still not optimal methode...currently working on it
#You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=[int(x) for x in nums]
        nums.sort()
        n=[nums[len(nums)-k]]
        n=[str(x) for x in n]

        return(n[0])
