'''
Implement two types of sorting algorithms: Merge sort and and bubble sort
'''
def merge_sort(list1):
    '''
    Merge sort function that sorts the values in a list using recursive calls.
    Input: a list of unsorted values
    Ouput: returns a list that is sorted.
    '''
    if len(list1) <=1:
        return list1
    mid = len(list1)//2
    l = list1[:mid]
    r = list1[mid:]

    merge_sort(l)
    merge_sort(r)
    list1 = merge(l,r, list1)
    return list1



def merge(l,r, list1):
    '''
    Function that merges to lists into one that is sorted in increasing order.
    Inputs: 3 lists, two that are being merged into the third.
    Output: Returns a merged list
    '''
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            list1[k] = l[i]
            i +=1
        else:
            list1[k] = r[j]
            j +=1
        k+=1
    
    while i < len(l):
        list1[k] = l[i]
        i+=1
        k+=1
    while j < len(r):
        list1[k] = r[j]
        j +=1 
        k +=1

    return list1


def print_list(list1):
    '''
    Function that prints out the contents of a list
    Inputs: a list
    Outputs: displays the list to the screen
    '''
    for i in range(len(list1)):
        print(list1[i], end = " ")
    print()

def bubble_sort(list1):
    n = len(list1)

    for i in range(n):

        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1


list1 = [1,98,55,6,34,23,45,68,76,2,3,4,6,7,97,55,67]
list1 = merge_sort(list1)
list2 = bubble_sort(list1)
print_list(list1)
print_list(list2)



    
