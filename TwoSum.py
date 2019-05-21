class BruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j];  
class TwoPassHashTable:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable=dict();
        for i in range(len(nums)):
            hashTable[nums[i]]=i;
        #print(hashTable);
        for i in range(len(nums)):
            complement=target-nums[i];
            if((complement in nums) and  (hashTable[complement]!=i)):
                return(i,hashTable[complement])
class OnePassHashTable:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable={};
        #print(hashTable);
        for i in range(len(nums)):
            complement=target-nums[i];
            if(complement in hashTable):
                return(hashTable[complement],i)
            hashTable[nums[i]]=i;
