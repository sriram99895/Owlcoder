class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        pre = []
        d ={}
        c = 0
        if(len(nums)==1 and nums[0]==k): return 1
        for i in nums:
            s+=i
            pre.append(s)
        p = 0
        # for i in range(len(nums)):
            # if(pre[i]==k and nums[i]==k): c+=1
            # p+=nums[i]
            # if p == k:
            #     c+=1
            #     if k in d:
            #         c+=len(d[k])
            # elif p-k in d:
            #     c+=len(d[p-k])  
            # if p in d:
            #     d[p].append(i)
            # else:
            #     d[p] = [i]     
            # if(pre[i]==k and nums[i]==k): c+=1
            # if pre[i] == k:
            #     c+=1
            #     if k in d:
            #         # print(len(d[k]))
            #         c+=len(d[k])
            # elif pre[i] - k in d:
            #     c+=len(d[pre[i]-k])
            # if pre[i] in d:
            #     d[pre[i]].append(i)
            # else:
            #     d[pre[i]] = [i]


        for i in range(len(nums)):
            p+=nums[i]
            if(p==k): c+=1
            if p-k in d:
                c+=d[p-k]
            if p in d:
                d[p]+=1
            else:
                d[p]=1
        
        # print(d)
        return c                   
        