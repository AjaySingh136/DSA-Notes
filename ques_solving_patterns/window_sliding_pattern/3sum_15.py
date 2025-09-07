from typing import List


class Solution:
    def Bruteforce_threeSum(self, nums: List[int]) -> List[List[int]]:
        ##Very Very Slow
        """
        Complexit = O(n^3) * log(n)
        """
        n = len(nums)-1
        idx = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        idx.append([nums[i] , nums[j] , nums[k]])
        return list({tuple(sorted(x)) for x in idx})

    def hashing_threeSum2(self, nums: List[int]) -> List[List[int]]:
        ##A Bit Faster
        """
        a + b + c = 0
        c = -(a+b)
        taget we can take as c and then need to search other 2 using hashing
        """
        ls = []
        end = len(nums)

        for i in range(end):
            target = -1 * nums[i]
            s = set() 
            for j in range((i+1), end):
                tofind = target - nums[j]
                if tofind in s:
                    trip = [nums[i], nums[j], tofind]
                    ls.append(trip)
                s.add(nums[j])
        return {tuple(sorted(x)) for x in ls}
    


    def threeSum_2pointers(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        ls = []
        for i in range(size):
            # Skip duplicate 'i' values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Since sorted, if nums[i] > 0, no possible triplet
            if nums[i] > 0:
                break
            j = i + 1
            k = size - 1
            while j < k:
                sum_trip = nums[i] + nums[j] + nums[k]
                if sum_trip < 0:
                    j += 1
                elif sum_trip > 0:
                    k -= 1
                else:
                    ls.append([nums[i], nums[j], nums[k]])
                    # Move j/k to next unique values
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum_2pointers(nums=nums))        
