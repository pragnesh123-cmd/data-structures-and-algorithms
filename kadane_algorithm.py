# function for kadane's algorithm
def kadane(MyList):
  max_sum = 0
  current_sum = 0
  for i in MyList:
    current_sum = current_sum + i
    if current_sum < 0:
      current_sum = 0
    if max_sum < current_sum:
      max_sum = current_sum
  return max_sum
  
# test the code
MyList = [-3, 1, -8, 12, 0, -3, 5, -9, 4]
print("Maximum SubArray is:",kadane(MyList))
