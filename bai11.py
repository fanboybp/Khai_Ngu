def soluongphantukhongtangnhieunhat(lst):
    max_count = 1  # Số lượng các phần tử không tăng nhiều nhất (tối thiểu là 1 với một phần tử)
    current_count = 1  # Số lượng hiện tại của các phần tử không tăng
    
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1
    
    return max_count

# Example usage:
mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]
print("Số lượng các phần tử không tăng nhiều nhất:", soluongphantukhongtangnhieunhat(mlist))