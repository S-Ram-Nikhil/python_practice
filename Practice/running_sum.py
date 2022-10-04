# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]

nums = [1,2,3,4]
output=[]
sum=0
for i in range(len(nums)):
    sum+=nums[i]
    output.append(sum)
print(output)



