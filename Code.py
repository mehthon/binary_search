def binary_serach():
    l = []
    target = int(input("Enter lost data: "))
    index_of_list = int(input("Enter your list range: "))
    for i in range(index_of_list):
        x = int(input())
        l.append(x)
    start = 0
    counter = 0
    end = len(l) - 1
    mid = (start + end) // 2
    while True:
        counter += 1
        if mid != start:
            if l[mid] < target:
                start = mid+1
                mid = (start + end) // 2
            elif l[mid] > target:
                end = mid - 1
                mid = (start + end) // 2
            else:
                index = mid
                break
        else:
            if target == l[start]:
                index = start
                break
            else:
                index = end
                break
    print("The target index is {} with number of {} total compare".format(index,counter))

binary_serach()



