class Solution:
    def sortPeople(self, names, heights):
        combined = list(zip(names, heights))
        combined.sort(key=lambda x: x[1], reverse=True)
        return [person[0] for person in combined]