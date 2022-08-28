##1
def qsort(arr):
   if len(arr) <= 1:
      return arr
   else:
      return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])
      
print(qsort([12, 11, 13, 5, 6, 7]))  



##2
def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []
 
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else: # if x > pivot
                greater.append(x)
        
        # Don't forget to return something!
        return sort(less) + equal + sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
        
print(sort())
