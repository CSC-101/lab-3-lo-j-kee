def tally(nums):
    total=0
    for num in nums:
        total=total+num
    # Iteration 1: total=0, total=0+4=4
    # Iteration 2: total=4, total=4+9=13
    # Iteration 3: total=13, total=13+2=15
    # Iteration 4: total+15, total=15+1=16
    return total

result = tally([4,9,2,1])
print(result)


def copy(nums):
    new_list=[]
    for idx in range(len(nums)): # len(nums) = 4
        new_list.append(nums[idx])
    # Iteration 1: idx=0, new_list.append(nums[0]) = [4]
    # Iteration 2: idx=1, new_list.append(nums[1]) = [4,9]
    # Iteration 3: idx=2, new_list.append(nums[2]) = [4,9,2]
    # Iteration 4: idx=3, new_list.append(nums[3]) = [4,9,2,1]
    return new_list

result = copy([4,9,2,1])
print(result)


def increment_all(nums):
    new_list=[]
    for value in nums:
        new_list.append(value+1)
    # Iteration 1: value=4, new_list.append(4+1) = [5]
    # Iteration 2: value=9, new_list.append(9+1) = [5,10]
    # Iteration 3: value=2, new_list.append(2+1) = [5,10,3]
    # Iteration 4: value=1, new_list.append(1+1) = [5,10,3,2]
    return new_list

result = increment_all([4,9,2,1])
print(result)