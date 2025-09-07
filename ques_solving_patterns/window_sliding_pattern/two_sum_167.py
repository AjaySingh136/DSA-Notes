
"""
Suppose if need get the max value in each sliding window of k 

k = 3
arr = [1,3,-1,-3,5,3,6,7]

start = 0
end = 0
max_ls = []
for i in range(len(arr)):
    start = i
    end = i
    end += k
    if end <= len(arr):
        ls = arr[start:end]
        max_ls.append(max(ls))

print(max_ls)
"""
"""#check if the string is pallendrome or not
def chkifpallendrome(s):
    
    i,j = 0,len(s)-1
    while (i<j):
        if (s[i] != s[j]):
            return False
        i+=1
        j-=1
    return True

print(chkifpallendrome('qwertytrewq'))
print(chkifpallendrome('qwert'))
print(chkifpallendrome('qwertiiiiiooo'))"""

#q - 167. Two SUM II - Input Array Is Sorted
from typing import List
class Solution:
    def twoSum_bad_solution(self, numbers: List[int], target: int) -> List[int]:
        arr = numbers
        output = []
        set_end = len(numbers)-1
        for i in range(0, len(numbers) ):
            end = set_end
            while (end > i):
                print(f"i = {i} and end = {end} and output = {output}")

                if (arr[end]+arr[i]) == target:
                    output = list((i+1,end+1))
                    break
                end -= 1
            if len(output) >0:
                break
        return output
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while (start < end):
            sum_num = (numbers[start] + numbers[end])
            # print(sum_num , numbers[start] , numbers[end])
            if sum_num == target :
                return list((start + 1, end + 1))
            if sum_num < target :
                start+=1
            if sum_num > target:
                end -=1

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([2,3,4], 6))
print(Solution().twoSum([-1,0], -1))
print(Solution().twoSum([-5,-3,0,2,4,6,8], 5))