import numpy as np
# ----FUNCTIONS----

# Function to check if the Array given can be splitted.
# input: array to analize.
# output: Can be splitted (1), Can´t be splitted (-1), Empty array (0)
def canBeSplitted (array):
    output = -1
    if array.size != 0:
        total = np.sum(array)
        start = 0
        i = 0
        arraySize = array.size
        while i < arraySize:
            start += array[i]
            total -= array[i]
            if start == total:
                output = 1
                break
            i += 1
    else:
        output = 0
    return output
    
# Function to find the position where the array can be splitted 
def splitIndex (array):
    total = np.sum(array)
    start = 0
    i = 0
    arraySize = array.size
    while i < arraySize:
        start += array[i]
        total -= array[i]
        if start == total:
            Index = i
            break
        i += 1
    if i >= arraySize:
        Index = None
    return Index

# ----TEST USER ARRAY----

userArray =  np.array([],int)
n = int(input("Enter The length of the array: "))
for i in range (n):
    x = int(input("Enther the "+ str(i+1) +" element for an Array:"))
    userArray = np.append(userArray, x)
print("The array to analyze is:", userArray)

if canBeSplitted(userArray) == 1:
    print("The array can be splitted.")
    Index = splitIndex(userArray)
    leftPart = np.zeros((Index + 1),int)
    rightPart = np.zeros((userArray.size - Index - 1),int)
    for i in range (Index + 1):
        leftPart[i] = userArray[i]
    for i in range (userArray.size - Index - 1):
        rightPart[i] = userArray[i + Index + 1]
    print("The left part is:", leftPart, " and the right part is: ", rightPart)
elif canBeSplitted(userArray) == -1:
    print("The array can't be splitted.")
else:
    print("The array is empty")
