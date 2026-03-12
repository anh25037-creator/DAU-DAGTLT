class Solution:
    def sortPeople(self, names, heights):
        return [x for _,x in sorted(zip(heights,names), reverse=True)]