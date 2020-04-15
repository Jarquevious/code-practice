"""Given a list of n numbers, determine if it contains any duplicate numbers."""
# Restate Question
# So I am given a list of numbers and I should determine if dupliactes are in this list?

# Clarifying Question
# For example, if I had nums = [5,6,3,8,2], I'll return no since it has none
# And = [3,6,2,7,4,7] return Yes, 7.
# Should I return the new list?

# Assumptions
# We have room for memory

# Brainstorm Solution
# We could sort the list and add duplicates to another list
# We could compare every value in the list 
# We could create a dictionary and count the frequency of each number and return key value pairs
# We Could use Binary search to find duplicates

# Explain Rational
# We can sort, loop. For each duplicate we will add to a new list. This is a o(1) runtime.
# Discuss Tradeoffs
# We trade memory for speed because we create a new list
# Suggest Improvements
# For speed I would say use a hash map to find duplicate. 

def find_duplicate(nums):
    # Create an empty array
    new_nums = []
    # loop through nums
    for num in nums:
        # if num not in nums
        if num in new_nums:
            # return num
            return num
        new_nums.append(num)
    return new_nums
    
   

nums = [3,6,2,7,4,7]
print(find_duplicate(nums))