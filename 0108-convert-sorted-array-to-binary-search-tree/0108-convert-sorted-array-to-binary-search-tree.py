# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums):

        # hàm đệ quy xây dựng cây từ đoạn nums[left:right]
        def build(left, right):

            # nếu không còn phần tử nào trong đoạn
            if left > right:
                return None

            # chọn phần tử giữa làm node gốc để đảm bảo cây cân bằng
            mid = (left + right) // 2

            # tạo node gốc với giá trị ở vị trí mid
            root = TreeNode(nums[mid])

            # xây cây con bên trái (các phần tử nhỏ hơn mid)
            root.left = build(left, mid - 1)

            # xây cây con bên phải (các phần tử lớn hơn mid)
            root.right = build(mid + 1, right)

            # trả về node gốc của cây con hiện tại
            return root

        # bắt đầu xây cây từ toàn bộ mảng
        return build(0, len(nums) - 1)