class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        ans=[0]*n
        pr_time=0
        
        for i in logs:
            x= i.split(":")
            fid= int(x[0])
            opt=x[1]
            timestamp=int(x[2])
            if opt=="start":
                if stack:
                    ans[stack[-1]]+=timestamp-pr_time
                stack.append(fid)
                pr_time=timestamp
            else:
                ans[stack[-1]]+=timestamp-pr_time+1
                stack.pop()
                pr_time=timestamp+1
        return ans
        
        
