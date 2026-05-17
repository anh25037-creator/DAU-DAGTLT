class Solution:
    def reverseList(self, head):
        # node trước đó (ban đầu không có)
        prev = None

        # node hiện tại bắt đầu từ head
        curr = head

        # duyệt đến khi hết list
        while curr:
            # lưu lại node tiếp theo
            next_node = curr.next

            # đảo chiều con trỏ
            curr.next = prev

            # di chuyển prev và curr tiến lên
            prev = curr
            curr = next_node

        # prev là head mới của danh sách đã đảo
        return prev