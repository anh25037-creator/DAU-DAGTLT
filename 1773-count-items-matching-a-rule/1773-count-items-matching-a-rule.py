class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2

        for item in items:
            if item[index] == ruleValue:
                count += 1

        return count