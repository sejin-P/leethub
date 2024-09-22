class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        n = self.trie
        
        for s in word:
            if s not in n:
                n[s] = {}
            n = n[s]
        
        n["$"] = True

    def search(self, word: str) -> bool:
        def search_node(word, node) -> bool:
            for i in range(len(word)):
                if word[i] not in node:
                    if word[i] == ".":
                        for key in node:
                            if key != "$" and search_node(word[i+1:],node[key]):
                                return True
                    
                    return False
                else:
                    node = node[word[i]]
            
            return "$" in node
        
        return search_node(word, self.trie)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)