def start_of_longest_positive_sequence(lst):
    vtrimax = -1  # Vị trí bắt đầu của đoạn số dương liên tiếp có nhiều phần tử nhất
    maxdem = 0  # Số lượng các số dương liên tiếp có nhiều nhất
    vitrihientai = -1  # Vị trí bắt đầu của đoạn số dương liên tiếp hiện tại
    dem = 0  # Số lượng các số dương liên tiếp hiện tại
    
    for i, num in enumerate(lst):
        if num > 0:
            if dem == 0:  # Nếu đây là phần tử đầu tiên trong đoạn số dương liên tiếp mới
                vitrihientai = i
            dem += 1
            if dem > maxdem:
                maxdem = dem
                vtrimax = vitrihientai
        else:
            dem = 0  # Đặt lại số lượng khi gặp số không dương
    
    return vtrimax

mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]
vtridautien = start_of_longest_positive_sequence(mlist)
if vtridautien != -1:
    print("Vị trí bắt đầu của đoạn số dương liên tiếp có nhiều phần tử nhất là:", vtridautien)
else:
    print("Không có đoạn số dương liên tiếp trong danh sách.")