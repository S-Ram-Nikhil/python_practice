# nums = [-1, 2, 3, 4, -5, -3] # find nearest value of zero
# pos_nums=[]
# neg_nums=[]
# i=0
# # using while loop
# while i<len(nums):
#     # print(nums[i])
#     if nums[i]>0:
#         pos_nums.append(nums[i])
#
#     else:
#         neg_nums.append(nums[i])
#     i+=1

#using for loop
# for num  in nums:
#     if num >=0 :
#         pos_nums.append(num)
#
#     else:
#         neg_nums.append(num)

# print(pos_nums)
# print(neg_nums)
#
# if min(pos_nums)+max(neg_nums)<0:
#     print(min(pos_nums))
# else:
#     print(max(neg_nums))



# l = [237,72,-18,237,-15,435, 99]
# out = min((abs(x), x) for x in l)[1]
# print(out)
l = [237,72,-18,237,-15,435, 99]
out = min(l, key=abs)
print(out)
