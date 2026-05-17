class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # =========================
        # 1. TÌM NODE Ở GIỮA LIST
        # =========================
        slow, fast = head, head

        # slow đi 1 bước, fast đi 2 bước
        # khi fast tới cuối thì slow ở giữa
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # =========================
        # 2. ĐẢO NGƯỢC NỬA SAU LIST
        # =========================
        prev = None
        curr = slow.next  # bắt đầu từ nửa sau

        slow.next = None  # cắt list làm 2 nửa

        while curr:
            nxt = curr.next  # lưu node kế tiếp
            curr.next = prev  # đảo chiều liên kết
            prev = curr
            curr = nxt

        # prev lúc này là head của nửa đã đảo

        # =========================
        # 3. TRỘN 2 NỬA LẠI VỚI NHAU
        # =========================
        first = head        # nửa đầu
        second = prev       # nửa sau (đã đảo)

        while second:
            tmp1 = first.next   # lưu node tiếp theo của first
            tmp2 = second.next  # lưu node tiếp theo của second

            # nối xen kẽ
            first.next = second
            second.next = tmp1

            # di chuyển con trỏ
            first = tmp1
            second = tmp2