my_list = [-1.2, 18.9, 23, 12.4, 17.6, 23.5, 12.2, 20.6, 11.5, 45.6]
i = int(input())
if i >= 0 and i <= len(my_list) - 1:
    print("Phần tử thứ", i, "từ cuối lên của danh sách có giá trị là",
          str(my_list[-i]) + ".")
elif i >= -len(my_list) and i <= -1:
    print("Phần tử thứ", i, "từ cuối lên của danh sách có giá trị là",
          str(my_list[-i - 1]) + ".")
else:
    print(i, "list index out of range")
