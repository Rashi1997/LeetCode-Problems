class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        level = ['']
        
        kvmaps = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
            } 
        for num in digits:
            level = [l + char for l in level for char in kvmaps[num]]
        return level if digits else []
        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        kvmaps = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
            } 
        res = []
        def DFS(i,path):
            if i == len(digits):
                res.append(path)
                return 
            for char in kvmaps[digits[i]]:
                DFS(i+1,path+char)
        DFS(0,'')
        return res if digits else []
