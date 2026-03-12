class Solution:
    def capitalizeTitle(self, title):
        words = title.split()
        res = []
        
        for w in words:
            if len(w) <= 2:
                res.append(w.lower())
            else:
                res.append(w[0].upper() + w[1:].lower())
                
        return " ".join(res)