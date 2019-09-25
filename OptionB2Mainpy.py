import time
import collections
from collections import OrderedDict

class Node(object):

   # Initializes the lists 
    def __init__(self):
        self.passwords = []
        self.duplicates = []
        self.duplicateAmount = 0

        self.BdictioDuplicates = {}
   # Solution A will use a for loop to increase the counter if a word is a duplciate. If the word is not a duplicate then it will be added to the linked list
    def SolutionA(self, password):
        for i in range(len(password)):
            if password[i] in self.passwords:
                self.duplicateAmount += 1
                self.duplicates.append(password[i])
            else:
                self.passwords.append(password[i])
   # Solution B will do the same as solution A but use a dictionary instead.
    def SolutionB(self, password):
        for i in range(len(password)):
            if password[i] in self.passwords:
                self.duplicateAmount += 1
                self.duplicates.append(password[i])
            else:
                self.passwords.append(password[i])

    def CleanerA(self):
        print("I found {} duplicates, and I searched {} passwords".format(self.duplicateAmount, len(self.passwords)))
        c = collections.Counter(self.duplicates)
        print("The top 20 passwords are: \n")
        i = 0
        mostCommon = []
        for name, score in c.most_common(20):
            i+=1
            mostCommon.append("{}.Password \"{}\" was found {} times\n".format(i, name.rstrip(), score))
        for i in range(len(mostCommon)):
            print(mostCommon[len(mostCommon) - (i + 1)])

    def CleanerB(self):
        for item in self.duplicates:
            if item in self.BdictioDuplicates:
                self.BdictioDuplicates[item] = self.BdictioDuplicates[item] + 1
            else:
                self.BdictioDuplicates[item] = 1

        arr = []
        for item in self.BdictioDuplicates:
            arr.append(self.BdictioDuplicates[item])

        return arr

    def DisplayResultsB(self, results):
        i = 0
        arr = []
        for result in results:
            i += 1
            if i > 20:
                break
            for name, number in self.BdictioDuplicates.items():
                if result == number:
                    arr.append("{}.Password \"{}\" was found {} times\n".format(i, name.rstrip(), number))
                    break
        for i in range(len(arr)):
            print(arr[len(arr) - (i + 1)])




def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all elements in array
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if element found is greater than the next
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

with open("10-million-combos.txt", 'r', encoding="utf-8", errors='ignore') as txt:
     # This code is for the Solution B
    # print("Work started on solution B.\nNothing will show up until finished to keep everything optimized.\n")
    # start_time = time.time()
    # engine = Node()
    # for i in range(10000):
        # engine.SolutionB(txt.readline().split('\t'))
    # results_to_merge = engine.CleanerB()
    
    # results = list(OrderedDict.fromkeys(mergeSort(results_to_merge)))
    # correct_results = []
    # for i in range(len(results)):
        # correct_results.append(results[len(results) - (i + 1)])
    # print("These are the top 20 passwords\n")
    # engine.DisplayResultsB(correct_results)
    
    # print("Done")
    # print("This took ", "{0:.2f} Seconds".format(time.time() - start_time))

    # Solution A code
    start_time = time.time()
    print("Work started on solution A.\nNothing will show up until finished to keep everything optimized.\n")
    engine = Node()
    # Change range to test other cases that are not 10 million. 10 million will take forever to run 
    for i in range(15000):
        # .split splits the passwords into two categories: first and last
        engine.SolutionA(txt.readline().split('\t'))
    print("Done")
    print("This took ", "{0:.2f} Seconds".format(time.time() - start_time))
    engine.CleanerA()