import heapq

class Solution:
    def pickGifts(self, gifts, k):
        
        # tạo max heap bằng số âm
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        
        for _ in range(k):
            
            # lấy phần tử lớn nhất
            largest = -heapq.heappop(heap)
            
            # tính floor(sqrt)
            reduced = int(largest ** 0.5)
            
            # đẩy lại vào heap
            heapq.heappush(heap, -reduced)
        
        # tính tổng còn lại
        return -sum(heap)