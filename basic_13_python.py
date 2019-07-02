#print 1-255
for x in range (1, 256, 1):
    print(x)


#print all odd integers from 1 to 255

def printOdds1To255():
    for i in range(1, 256, 1):
        if i % 2 != 0:
            print(i)

#iterate through a given list, printing each value

def printListVals(list):
    for i in range(0, len(arr), 1):
        print(list[i])

#create a list with all the odd integers between 1 and 255 (inclusive)

def returnOddsList1To255():
    new_list = []
    for i in range (1, 256, 1):
        if i % 2 != 0:
            new_list.append(i)
    print(new_list)

#square each value in a given list, returning that same list with changed values 

def squareListVals(list):
    for i in range(0, len(list), 1):
        list[i] = list[i] * list[i]
    return list

#print integers from 0 to 255, and with each integer print the sum so far

def printIntsAndSum0To255():
    sum = 0
    for i in range(0, 256, 1):
        sum = sum + i
        print(i)
        print(sum)

#analyze a list's value and print the average

def printAverageOfList(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
        average = sum / len(list)
    print(average)

#print max of list

def printMaxOfList(list):
    max = list[0]
    for x in range (0, len(list), 1):
        if (max < list[x]):
            max = list[x]
    print(max)
    
#print max, min, average list values

def maxMinAvg(list):
    max = list[0]
    min = list[0]
    sum = 0
    for x in range (0, len(list), 1):
        if (max < list[x]):
            max = list[x]
        if (min > list[x]):
            min = list[x]
        sum = sum + list[x]
        avg = sum / len(list)
    new_list = [max, min, avg]
    print(new_list)

#given a list and a value for y, count and print the number of list values greater than y

def returnListCountGreaterThanY(list, y):
    count = 0
    for i in range(0, len(list), 1):
        if (list[i] > y):
            count = count + 1
    print(count)

#given a list, move all values forward (to the left) by one index, dropping the first value and leaving a 0 value at the end of the array

def shiftListValsLeft(list):
    for i in range(0, len(list) - 1, 1):
        list[i] = list[i + 1]
    list[- 1] = 0
    return list

#given a list of numbers, replace any negative values with the string 'Dojo'

def swap(list):
    for i in range(0, len(list), 1):
        if list[i] < 0:
            list[i] = "Dojo"
    print(list)

#return the list after setting any negative values to zero

def zeroOutNegVals(list):
    for i in range(0, len(list), 1):
        if list[i] < 0:
            list[i] = 0
    print(list)