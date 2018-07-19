class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def manacher(s):
            s = '#' + '#'.join(s) + '#'
            RL = [0]*len(s)
            maxRight = 0
            pos = 0
            maxLen = 0
            for i in range(len(s)):
                if i<maxRight:
                    RL[i] = min(RL[2*pos-i], maxRight - i)
                else:
                    RL[i] = 1
                while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]] == s[i+RL[i]]:
                    RL[i] += 1
                if RL[i]+i-1 > maxRight:
                    maxRight = RL[i]+i-1
                    pos = i
                if maxLen < RL[i]:
                    maxPos = i
                maxLen = max(maxLen, RL[i])
            return maxPos, maxLen - 1
        maxPos, maxLen = manacher(s)
        s = '#' + '#'.join(s) + '#'
        if maxLen%2 != 0:
            ans = s[maxPos]
            for i in range(2, int(maxLen), 2):
                ans = s[maxPos - i] + ans + s[maxPos + i]
        else:
            ans = ''
            maxLen+=1
            for i in range(2, int(maxLen), 2):
                ans = s[maxPos - i + 1] + ans + s[maxPos + i - 1]
        return ans
			

s = Solution()
print(s.longestPalindrome('cbbd'))