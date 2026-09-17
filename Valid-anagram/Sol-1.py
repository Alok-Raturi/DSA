class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapp = {}
        for i in s:
            x = mapp.get(i,0)
            mapp[i]=x+1
        for i in t:
            if i in mapp:
                mapp[i]-=1
                if mapp[i] == 0:
                    del mapp[i]
            else:
                return False
        return len(mapp) == 0
        