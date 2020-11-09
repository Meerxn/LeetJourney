'''

[-1,0,1,2,-1,-4]

[-4,-1,-1,0,1,2]

'''

def threeSum(nums):
    nums = sorted(nums)
    ans = [] 
    #defaul check on empty strings
    if len(nums) < 3:
        return []
    #making sure to not need to loop ahead    
    for i in range(len(nums) -2):
        #positive integer start means everything ahead is also posotive so no need
        if nums[i] > 0:
            return ans
        #Here we check whether every element is not repeated again (checking for a position repeats)
        if nums[i] == nums[i-1] and i > 0:
            continue  
        #left  
        b = i+1
        #rifht
        c = len(nums) -1
        while b < c:
            sumV = nums[i] + nums[b] + nums[c]
            if sumV == 0:
                ans.append([nums[i],nums[b],nums[c]])
                b += 1
                c -= 1
                while nums[b] == nums[b-1] and b < c:
                    b = b +1

                
            elif sumV > 0:
                c -= 1
            elif  sumV < 0:
                b += 1
        
    return ans
        
print(threeSum([-1,0,1,2,-1,-4]))
