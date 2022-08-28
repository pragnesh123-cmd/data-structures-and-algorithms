# Bubble sort in Python

#1 logic
def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)




#2 logic

def bubblesort(elements):
  # Looping from size of array from last index[-1] to index [0]
  for n in range(len(elements)-1, 0, -1):
    for i in range(n):
      if elements[i] > elements[i + 1]:
        # swapping data if the element is less than next element in the array
        elements[i], elements[i + 1] = elements[i + 1], elements[i]
elements = [39,12,18,85,888,72,10,2,18]
  
print("Unsorted list is,") 
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)
