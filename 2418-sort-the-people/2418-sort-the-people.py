class Solution:
    def sortPeople(self, names, heights):

        # Ghép chiều cao với tên
        people = []

        for i in range(len(names)):
            people.append([heights[i], names[i]])

        # Sắp xếp giảm dần theo chiều cao
        people.sort(reverse=True)

        # Mảng kết quả
        result = []

        # Lấy tên sau khi sắp xếp
        for height, name in people:
            result.append(name)

        # Trả về kết quả
        return result