# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string


def balconies():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    #evaluate the area of the two different balconies and determine which one is bigger
    #two string inputs separated by a comma the first string represents apartment a and
    # second string represents apartment b
    apartA = input('Please enter the dimensions of the apartment A: ')
    apartB = input('Please enter the dimensions of the apartment B: ')
    print(apartA, apartB)
    listA = list(apartA.split(","))
    print(listA)
    listB = list(apartB.split(","))
    print(listB)
    areaA = int(listA[0]) * int(listA[1])
    print(areaA)
    areaB = int(listB[0]) * int(listB[1])
    print(areaB)
    if(areaA > areaB):
        print("Area A is bigger")
    elif(areaB > areaA):
        print("Area B is bigger")
    else:
        print("Not applicable")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    balconies()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
