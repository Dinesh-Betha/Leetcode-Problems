class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        mp={"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        def validCode(s):
            if not s: return False
            for c in s:
                if not c.isalnum() and c!='_': return False
            return True

        def validB(s):
            if s not in mp: return -1
            return mp[s]
        ans=[[] for _ in range(4)]
        
        for i, x in enumerate(code):
            if isActive[i] and validCode(x) and (bi:=validB(businessLine[i]))>=0:
                ans[bi].append(x)
        return sorted(ans[0])+sorted(ans[1])+sorted(ans[2])+sorted(ans[3])

        