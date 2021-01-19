""" This is an optimized method of soriting based of from the insertion sorting algorithm discussed below """
def shell_sort(data):
    list_size = len(data)
    gap = list_size // 2

    while gap > 0:
        for i in range(gap, list_size):
            pointer  = data[i]
            j = i

            while j>gap and data[j-gap] > pointer:
                print("Looping")
                data[j] = data[j-gap]
                j -= gap

            data[j] = pointer
            
        gap = gap // 2

if __name__ == "__main__":
    x = ['a', 'e',  'b', 'c', 'd', 'i', 'j', 'k', 'l', 'f', 'g', 'h', 'm']
    shell_sort(x)
    print(x, "End result")