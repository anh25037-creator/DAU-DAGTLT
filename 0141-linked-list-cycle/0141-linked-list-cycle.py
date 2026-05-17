class Solution:
    def hasCycle(self, head):
        # Trường hợp đặc biệt:
        # nếu danh sách rỗng hoặc chỉ có 1 node thì không thể có chu trình
        if not head or not head.next:
            return False

        # slow: di chuyển từng bước (1 node/lần)
        slow = head

        # fast: di chuyển nhanh hơn (2 node/lần)
        fast = head

        # tiếp tục duyệt khi fast và fast.next còn tồn tại
        # (nếu fast hoặc fast.next = None → đã tới cuối list → không có cycle)
        while fast and fast.next:

            # slow đi 1 bước
            slow = slow.next

            # fast đi 2 bước
            fast = fast.next.next

            # nếu slow và fast gặp nhau
            # => có vòng lặp (cycle)
            if slow == fast:
                return True

        # nếu thoát vòng while nghĩa là fast đã tới None
        # => không có cycle
        return False