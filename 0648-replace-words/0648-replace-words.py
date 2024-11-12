class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x : len(x))
        splitted = sentence.split()
        
        for i in range(len(splitted)):
            for root in dictionary:
                if self.isDerivative(splitted[i], root):
                    splitted[i] = root
                    break
        
        return ' '.join(splitted)
        
    def isDerivative(self, word, root):
        return word[:min(len(word), len(root))] == root
        