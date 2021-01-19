""" This is a Custom Sorting Algorithm thou not efficient """
def insertion_sort(elements):
    for i in range(1, len(elements)):
        pointer = elements[i]
        j = i - 1
        while j >= 0 and pointer < elements[j]: #While j is greater than or equal to 0 and the current element is greater than the element indexed at it back
            elements[j+1] = elements[j] #converting the element index to be the in front of the pointer to the pointer element
            j = j - 1 
        elements[j+1] = pointer



if __name__ == "__main__":
    x = ['a', 'e',  'b', 'c', 'd', 'i', 'j', 'k', 'l', 'f', 'g', 'h', 'm']
    insertion_sort(x)
    print(x) #It is working