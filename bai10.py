def soluongphantudandau(lst):
    max_count = 0  # Số lượng các phần tử liên tiếp đan dấu nhiều nhất
    current_count = 0  # Số lượng hiện tại của các phần tử liên tiếp đan dấu
    
    for i in range(len(lst) - 1):
        if lst[i] * lst[i + 1] < 0:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count

# Example usage:
mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]
print("Số lượng các phần tử liên tiếp đan dấu nhiều nhất:", soluongphantudandau(mlist))