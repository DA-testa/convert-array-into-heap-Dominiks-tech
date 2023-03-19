# python3


def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    for i in range(n // 2, -1, -1):
        heap_sort(data, i, swaps)
    return swaps

def heap_sort(data, i, swaps):
    
    n = len(data)
    parent = i
    #nosaka vai kreisais "Child" atbilst nosacijumiem
    krChild =2*i+1

    if krChild <= (n-1) and data[krChild] < data[parent]:
        parent = krChild
    #nosaka vai labais "Child" atbild noscijumiem

    labChild =2*i+2  
    if labChild <= (n-1) and data[labChild] < data[parent]:
        parent = labChild
    if i != parent:
        #samaina 
        data[i], data[parent] = data[parent], data[i]
        #ievieto apmainu "swap"
        swaps.append(i, parent)
        #loopo lidz noteikts 
        heap_sort(data, parent, swaps)






def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    print("F vai I")
    fi = input()
    fi = fi.replace('\r\n', '\n')
    if fi == "F":
        fails =input()
        with open(fails,'r') as testfile:
            n = int(testfile.readline().strip())
            n1 = testfile.readline().strip()
        data = list(map(int, n1.split()))
        # print(n)
        # print(data)
    if fi == "I":
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
        # print(data)


    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    # print(swaps)
    # print(data)
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
