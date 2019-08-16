class my_Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return [""]
        return self.generate("",n,0)
    def generate(self,curr,num_available,num_unclosed):
        if num_available==0:
            return [curr +")" * num_unclosed]
        elif num_unclosed==0:
            return self.generate(curr +"(",num_available-1,num_unclosed+1)
        return (self.generate(curr +"(",num_available-1,num_unclosed+1) + self.generate(curr +")",num_available,num_unclosed-1))
        
class Closure_Number:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return [""]
        ans=[]
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append("({}){}".format(left,right))
        return ans
        
class Backtracking:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        if n==0:
            return [""]
        def backtrack(S='',left=0,right=0):
            if len(S)==2*n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(',left+1,right)
            if right< left:
                backtrack(S+')',left,right+1)
        backtrack()
        return ans
