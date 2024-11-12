class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        
        for word in dictionary:
            prev = trie
            for letter in word:
                if letter not in prev:
                    prev[letter] = {}
                prev = prev[letter]
            prev[''] = ''
        
        splitted = sentence.split()
        
        for i in range(len(splitted)):
            root = self.derivativeWord(trie, splitted[i])
            if root != '':
                splitted[i] = root
        
        return ' '.join(splitted)
        
    
    def derivativeWord(self, trie, word):
        prev = trie
        root = ''
        for letter in word:
            if letter not in prev:
                if '' in prev and prev[''] == '':
                    return root
                return ''
            prev = prev[letter]
            root += letter
            if '' in prev and prev[''] == '':
                return root
        
        if '' in prev and prev[''] == '':
            return root
        
        return ''
        
        
        