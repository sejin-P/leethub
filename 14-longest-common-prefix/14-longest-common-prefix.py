class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        prefix_length = len(prefix)
        for word in strs[1:]:
            length = min(len(word), prefix_length)
            new_prefix = ""
            for i in range(length):
                if prefix[i] == word[i]:
                    new_prefix += word[i]
                else:
                    break
            prefix = new_prefix
            prefix_length = len(prefix)
            
            
        return prefix
        