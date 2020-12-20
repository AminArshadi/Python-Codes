import random

def selection_sort(L):
     '''
     (list)->None
     sorts a given list L
     '''
     for i in range(len(L)-1):
          # Find the minimum in the list[i..len(L)-1]
          min_index=i
          for j in range(i+1, len(L)):
               if(L[min_index]>L[j]):
                    min_index=j
          
          #Swap L[i] with L[min_index] if necessary
          # (the line of code below does basicaly nothing if L[i] is the mininum)
          L[i],L[min_index]=L[min_index], L[i]


#########################################################################################################
#########################################################################################################


# recursive mergesort

def merge_sort(L):
    if len(L)<2:
        return L[:]
    else:
        middle =len(L)//2
        left=merge_sort(L[:middle])
        right=merge_sort(L[middle:])
        return merge(left,right)



def merge(L1, L2):
     """ (list, list) -> list
     Merge sorted lists L1 and L2 into a new list and return that new list.
     >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
     [1, 1, 2, 3, 4, 5, 6, 7]
     """
     newL = []
     i1 = 0
     i2 = 0
     # For each pair of items L1[i1] and L2[i2], copy the smaller into new L.
     while i1 != len(L1) and i2 != len(L2):
          if L1[i1] <= L2[i2]:
               newL.append(L1[i1])
               i1 =i1+ 1
          else:
               newL.append(L2[i2])
               i2=i2+ 1
     # Gather any leftover items from the two sections.
     # Note that one of them will be empty because of the loop condition.
     newL.extend(L1[i1:])
     newL.extend(L2[i2:])
     return newL



#########################################################################################################
#########################################################################################################



def qs(a):
    """Return a sorted copy of a"""
    if len(a) == 0:
        return []
    x = random.choice(a)
    lt, eq, gt=[],[],[]
    
    for item in a:
         if item < x:
             lt.append(item)
         elif item == x:
             eq.append(item)
         else:
             gt.append(item) 
    return qs(lt) + eq + qs(gt)


#########################################################################################################
#########################################################################################################

import time
def print_times(L):
     '''list->None'''
     
     # my quick sort:
     print("MY MERGE SORT:")
     copy=L[:]
     t1=time.perf_counter()
     merge_sort(copy)
     t2=time.perf_counter()
     print(t2-t1)

     # my quick sort:
     print("MY QUICK SORT:")
     copy=L[:]
     t1=time.perf_counter()
     qs(copy)
     t2=time.perf_counter()
     print(t2-t1)
     
     #python's sort
     print("PYTHON SORT:")
     copy=L[:]
     t1=time.perf_counter()
     copy.sort()
     t2=time.perf_counter()
     print(t2-t1)

     #my selection sort
     print("MY SELECTION SORT:")
     copy=L[:]
     t1=time.perf_counter()
     selection_sort(copy)
     t2=time.perf_counter()
     print(t2-t1)
     
#print("EXPERIMENT with sorting a list of 100,000 random numbers")

#lst=random.sample(range(1000000), 100000)
#print_times(lst)
