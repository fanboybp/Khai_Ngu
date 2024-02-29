def chen_danh_sach_vao_vitri(danh_sach, vitri, danh_sach_chen):
    danh_sach[vitri:vitri] = danh_sach_chen #tạo vùng trích xuất có giá trị bằng danh sách chèn ví dụ nó sẽ trích xuất từ vị trí 0 1 2 cho danh sách chèn 1 2 3

# Đọc danh sách từ người dùng (ví dụ)

mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]
# Danh sách cần chèn
danh_sach_chen = [1, 2, 3]

# Chèn danh sách vào đầu, cuối và vị trí thứ 5 của danh sách
chen_danh_sach_vao_vitri(mlist, 0, danh_sach_chen)  # Chèn vào đầu
chen_danh_sach_vao_vitri(mlist, len(mlist), danh_sach_chen)  # Chèn vào cuối
chen_danh_sach_vao_vitri(mlist, 4, danh_sach_chen)  # Chèn vào vị trí thứ 5

# In danh sách đã chèn ra màn hình
print("Danh sách sau khi chèn danh sách [1, 2, 3] vào đầu, cuối và vị trí thứ 5:")
print(mlist)