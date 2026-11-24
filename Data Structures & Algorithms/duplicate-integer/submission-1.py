class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newNums = []
        for i in nums:
            newNums.append(nums[i])
            if newNums[i] == nums[i]:
                print("False")
            else:
                print("True")



         