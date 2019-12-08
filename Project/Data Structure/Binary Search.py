
def Binary_Search( my_list , item ):
    l = 0 #下标
    r = len(my_list) -1 #下标
    while l <= r: # <= 不加括号
        mid = (l + r) // 2 # 注意 middle 要为整数
        if my_list[mid] < item:
            l = mid + 1
        elif my_list[mid] > item:
            r = mid - 1
        else:
            return mid
    return None

if __name__ == '__main__':
        my_list= [1, 3, 5, 7, 9]
        print(Binary_Search(my_list, 3))  # 打印3索引值的索引值 => 1
        print(Binary_Search(my_list, -1)) # 未找到-1，打印None