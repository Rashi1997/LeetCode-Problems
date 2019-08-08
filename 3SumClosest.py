class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums=sorted(nums)
		res=float('inf')
		diff=float('inf')
		for i in range(len(nums)):
			start=i+1
			end=len(nums)-1
			while start<end:
				sum1=nums[i]+nums[start]+nums[end]
				if diff>abs(target-sum1):
					res=sum1
				diff=min(diff,abs(target-res))
				if res==target:
					break
				if sum1>target:
					end-=1
				else:
					start+=1
		return res
