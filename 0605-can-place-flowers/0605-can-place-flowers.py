#Không được trồng 2 bông hoa cạnh nhau
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        
        # Đếm số hoa có thể trồng thêm
        count = 0
        
        # Duyệt từng vị trí
        for i in range(len(flowerbed)):
            
            # Kiểm tra ô bên trái
            left_empty = (i == 0 or flowerbed[i - 1] == 0)
            
            # Kiểm tra ô bên phải
            right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            
            # Nếu vị trí hiện tại trống
            # và 2 bên đều trống
            if flowerbed[i] == 0 and left_empty and right_empty:
                
                # Trồng hoa tại đây
                flowerbed[i] = 1
                
                # Tăng số lượng hoa đã trồng
                count += 1
        
        # Nếu trồng được ít nhất n bông hoa
        return count >= n