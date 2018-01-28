# data = [7, 5, 10, 8]
#
# doan = int(input("Enter a number: "))
#
# for i in range(len(data)):
#     if doan == data[i]:
#         print("Found {} at index {}".format(doan, i))
#         break
#     else:
#         continue
# else:
#     print("Not found")


# Cach 1
# nums = [7, 5, 10, 8, 200, 30]
#
# num_to_find = int(input("Enter a number? "))
#
# if num_to_find in nums: # 1 for
#     print("Found")
#     found_index = nums.index(num_to_find)
#     print("Index: ", found_index)
# else:
#     print("Not found")

# Cach 2
# nums = [7, 5, 10, 8, 200, 30]
#
# num_to_find = int(input("Enter a number? "))
#
# # 1. Assumption / Gia dinh ve ket qua
# found_index = -1 # not Found
#
# # 2. Create a loop to test our Assumption
# for index, num in enumerate(nums):
#     if num == num_to_find:
#         found_index = index # update Assumption
#         print("Found")
#         break
#
# #3. Print results
# if found_index == -1:
#     print("Not found")
# else:
#     print("Found at index", found_index)

# cach 3
nums = [7, 5, 10, 8, 200, 30]

num_to_find = int(input("Enter a number? "))

for index, num in enumerate(nums):
    if num == num_to_find:
        print("Found at index:", index)
        break
else:
    print("Not found")
