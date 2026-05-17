class Solution:
    def sortArray(self, nums):

        # Hàm dùng để gộp 2 mảng đã được sắp xếp
        def merge(left, right):

            # Mảng kết quả sau khi gộp
            result = []

            # Con trỏ cho mảng left
            i = 0

            # Con trỏ cho mảng right
            j = 0

            # So sánh từng phần tử của 2 mảng
            while i < len(left) and j < len(right):

                # Nếu phần tử bên trái nhỏ hơn
                if left[i] < right[j]:

                    # Thêm vào result
                    result.append(left[i])

                    # Di chuyển i sang phần tử tiếp theo
                    i += 1

                else:
                    # Nếu phần tử bên phải nhỏ hơn hoặc bằng
                    result.append(right[j])

                    # Di chuyển j
                    j += 1

            # Sau vòng while:
            # có thể left hoặc right vẫn còn phần tử

            # Thêm tất cả phần còn lại của left
            result.extend(left[i:])

            # Thêm tất cả phần còn lại của right
            result.extend(right[j:])

            return result


        # Hàm Merge Sort
        def mergeSort(arr):

            # Nếu mảng chỉ có 1 phần tử
            # thì đã tự sắp xếp rồi
            if len(arr) <= 1:
                return arr

            # Tìm vị trí giữa mảng
            mid = len(arr) // 2

            # Chia mảng thành 2 nửa
            left = arr[:mid]
            right = arr[mid:]

            # Đệ quy tiếp tục chia nhỏ
            left = mergeSort(left)
            right = mergeSort(right)

            # Gộp 2 mảng đã sắp xếp
            return merge(left, right)

        return mergeSort(nums)