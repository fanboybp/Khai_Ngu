def chuyen_phan_tu_duong_len_dau(danh_sach):
    # Tạo danh sách mới để chứa các phần tử dương
    phan_tu_duong = [x for x in danh_sach if x > 0]
    
    # Loại bỏ các phần tử dương từ danh sách ban đầu
    danh_sach = [x for x in danh_sach if x <= 0]
    
    # Nối danh sách các phần tử dương lên đầu danh sách ban đầu
    danh_sach = phan_tu_duong + danh_sach
    
    return danh_sach

# Đọc danh sách từ người dùng (ví dụ)
mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]

# Chuyển các phần tử dương lên đầu danh sách
danh_sach_da_chuyen = chuyen_phan_tu_duong_len_dau(mlist)

# In danh sách đã chuyển ra màn hình
print("Danh sách sau khi chuyển các phần tử dương lên đầu:")
print(danh_sach_da_chuyen)