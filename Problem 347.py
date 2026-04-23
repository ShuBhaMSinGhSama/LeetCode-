class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh={}
        ans=[]
        for x in nums:
            if x in hsh:
                hsh[x]+=1
            else:
                hsh[x]=1
        bucket = list([] for _ in range(len(nums)+1))
        for key, value in hsh.items():
            bucket[value].append(key)
        i=len(bucket)-1
        print(bucket)
        while len(ans) < k and i >= 0:
            if bucket[i]:
                for num in bucket[i]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
            i-=1
        return ans
