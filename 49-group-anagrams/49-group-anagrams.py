class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            sorted_word = str(sorted(word))
            prev = word_map.get(sorted_word)
            if prev is None:
                word_map[sorted_word] = [word]
            else:
                word_map[sorted_word].append(word)
        
        return word_map.values()
        
        