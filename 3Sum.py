class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_dic = {}

        sum_list = []

        for n in nums:
            if n in nums_dic:
                nums_dic[n] += 1
            else:
                nums_dic[n] = 1

        if 0 in nums_dic and nums_dic[0] > 2:
            sum_list.append([0, 0, 0])

        nums_neg = [k for k in nums_dic.keys() if k < 0]
        nums_pos = [k for k in nums_dic.keys() if k >= 0]

        for n in nums_neg:
            for p in nums_pos:
                target = -n-p
                if target in nums_dic:
                    if target in [n, p] and nums_dic.get(target) >=2:
                        sum_list.append([n, p , target])
                    
                    if target > p or target < n:
                        sum_list.append([n, p, target])

        return sum_list
