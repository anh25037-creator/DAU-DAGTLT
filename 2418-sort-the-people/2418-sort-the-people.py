class Solution:
    def sortPeople(self, names, heights):
        
        # ghép mỗi người thành cặp (tên, chiều cao)
        people = list(zip(names, heights))
        
        # sắp xếp theo chiều cao giảm dần
        people.sort(key=lambda x: x[1], reverse=True)
        
        # lấy lại danh sách tên sau khi đã sắp xếp
        return [name for name, height in people]