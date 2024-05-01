class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for p in (2,3,5):
            while n % p == 0 :
                n //= p 
        return n == 1
        

# n = 17輸入 由於不能被整除 n = 17 會被拿去做判斷是否 == 1 不是False
# n = 48 是否被整除 可以 n//p 會一直除到剩下1 也就是True
