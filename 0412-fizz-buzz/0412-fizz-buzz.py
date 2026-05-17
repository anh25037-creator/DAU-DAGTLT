class Solution:
    def fizzBuzz(self, n):

        # Tạo mảng rỗng để lưu kết quả
        answer = []

        # Duyệt các số từ 1 đến n
        for i in range(1, n + 1):

            # Kiểm tra nếu i chia hết cho cả 3 và 5
            # (% là phép chia lấy dư)
            # Nếu dư = 0 nghĩa là chia hết
            if i % 3 == 0 and i % 5 == 0:

                # Thêm "FizzBuzz" vào mảng
                answer.append("FizzBuzz")

            # Nếu chỉ chia hết cho 3
            elif i % 3 == 0:

                # Thêm "Fizz"
                answer.append("Fizz")

            # Nếu chỉ chia hết cho 5
            elif i % 5 == 0:

                # Thêm "Buzz"
                answer.append("Buzz")

            # Nếu không chia hết cho 3 hay 5
            else:

                # Đổi số thành chuỗi rồi thêm vào mảng
                answer.append(str(i))

        # Trả về mảng kết quả
        return answer