class Solution:
    def hasCycle(self, head):
        # nếu list rỗng hoặc chỉ có 1 node thì không có cycle
        if not head or not head.next:
            return False

        slow = head      # đi từng bước
        fast = head      # đi hai bước

        # duyệt đến khi fast hoặc fast.next hết
        while fast and fast.next:
            slow = slow.next          # đi 1 bước
            fast = fast.next.next     # đi 2 bước

            # nếu gặp nhau → có cycle
            if slow == fast:
                return True

        # đi đến cuối mà không gặp → không có cycle
        return False