class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 1:
            return path
        real_path = []
        str_li = path.split("/")
        print(str_li)
        for word in str_li:
            if len(word) == 0:
                continue
            if len(word) == 1:
                if word == ".":
                    continue
                real_path.append(word)
                continue
            
            if word == "..":
                if len(real_path) != 0:
                    real_path.pop()
                continue
            
            real_path.append(word)
        
        return "/"+"/".join(real_path)
        