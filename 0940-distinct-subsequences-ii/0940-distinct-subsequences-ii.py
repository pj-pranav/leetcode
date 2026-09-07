class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod=10**9+7
        dp=1
        last={}
        for ch in s:
            new_dp=(2*dp)%mod
            if ch in last:
                new_dp=(new_dp-last[ch])%mod
            last[ch]=dp
            dp=new_dp
        return (dp-1)%mod
        