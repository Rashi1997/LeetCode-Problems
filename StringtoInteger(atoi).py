class Solution:
    def myAtoi(self, str: str) -> int:
        l=str.split(" ")
        neg=1
        digits=''
        l=[x for x in l if x]
        if l==[]:
            return 0
        for x in range(len(l[0])):
            if((l[0][x]!="+" and l[0][x]!="-" and not l[0][x].isdigit())):
                break
            else:
                if (l[0][x]=='-' and x==0):
                    neg=-1
                elif(l[0][x].isdigit()):
                    digits+=l[0][x]
                elif((l[0][x]=='+' and x!=0)  or (l[0][x]=='-' and x!=0)):
                    break
                elif(l[0][x]=='.'):
                    break
        if digits=='':
            digits=0
        if (-(2**31))> neg*int(digits):
            return -(2**31)
        elif((neg*int(digits))>(2**31)-1):
            return (2**31)-1
        else:
            return (neg*int(digits))
