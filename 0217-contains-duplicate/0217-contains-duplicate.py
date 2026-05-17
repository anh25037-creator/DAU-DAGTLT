class Solution:
    def containsDuplicate(self, nums):

        # Tạo set để lưu các phần tử đã gặp
        seen = set()

        # Duyệt từng số trong mảng
        for num in nums:

            # Nếu số đã tồn tại trong set
            # => có phần tử trùng lặp
            if num in seen:
                return True

            # Nếu chưa có thì thêm vào set
            seen.add(num)

        # Duyệt hết mà không có phần tử trùng
        return False