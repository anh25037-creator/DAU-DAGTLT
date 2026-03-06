class Solution:
    def secondHighest(self, s):
        nums = []

        for c in s:
            if c.isdigit():
                nums.append(int(c))

        nums = list(set(nums))      # bỏ trùng
        nums.sort(reverse=True)     # sắp xếp giảm dần

        if len(nums) < 2:
            return -1
        else:
            return nums[1]