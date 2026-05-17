class Solution:
    def duplicateZeros(self, arr):
        
        # Duyệt từng phần tử trong mảng
        i = 0
        
        while i < len(arr):

            # Nếu gặp số 0
            if arr[i] == 0:

                # Chèn thêm một số 0 vào vị trí hiện tại
                arr.insert(i, 0)

                # Xóa phần tử cuối để giữ nguyên độ dài mảng
                arr.pop()

                # Bỏ qua số 0 vừa chèn thêm
                i += 1

            # Sang vị trí tiếp theo
            i += 1