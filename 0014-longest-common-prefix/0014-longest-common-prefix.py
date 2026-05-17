class Solution:
    def longestCommonPrefix(self, strs):
        
        # Nếu mảng rỗng
        if not strs:
            return ""
        
        # Lấy chuỗi đầu tiên làm prefix ban đầu
        prefix = strs[0]
        
        # Duyệt các chuỗi còn lại
        for s in strs[1:]:
            
            # Nếu chuỗi hiện tại không bắt đầu bằng prefix
            while not s.startswith(prefix):
                
                # Xóa ký tự cuối của prefix
                prefix = prefix[:-1]
                
                # Nếu prefix rỗng
                if prefix == "":
                    return ""
        
        return prefix