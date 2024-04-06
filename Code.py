class Solution:
    def numberOfMatches(self, n: int) -> int:
        i = 0
        while(n > 1):
            if n%2 == 0:
                i += n/2
                n = n/2
            else:
                i += n//2
                n = n//2 +1
        return int(i)
