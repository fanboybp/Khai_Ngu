def cacsoduonglientiepcotonglonnhat(lst):
    maxtong = 0  # Tổng lớn nhất của các số dương liên tiếp
    tong = 0  # Tổng hiện tại của các số dương liên tiếp
    maxdem = 0  # Số lượng các số dương liên tiếp có tổng lớn nhất
    dem = 0  # Số lượng hiện tại của các số dương liên tiếp có tổng lớn nhất
    
    for num in lst:
        if num > 0:
            tong += num
            dem += 1
        else:
            if tong > maxtong:
                maxtong = tong
                maxdem = dem
            elif dem > maxdem:
                maxdem = dem
            tong = 0
            dem = 0
    
    # Xử lý trường hợp khi danh sách kết thúc với một chuỗi số dương
    if tong > maxtong:
        maxtong = tong
        maxdem = dem
    elif tong == maxtong:
        maxdem = dem
        
    return maxdem

mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]
print("cac so duong lien tiep co tong nhieu nhat:", cacsoduonglientiepcotonglonnhat(mlist))