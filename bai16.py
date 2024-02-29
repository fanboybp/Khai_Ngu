def la_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def tim_so_duong_va_nguyen_to(danh_sach):
    ket_qua = []
    for i, x in enumerate(danh_sach):
        if x > 0 and la_so_nguyen_to(x):
            ket_qua.append((i, x))
    return ket_qua
mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]
ketqua=tim_so_duong_va_nguyen_to(mlist)
print("Các số dương và là số nguyên tố cùng với vị trí của chúng:")
for vi_tri, so in ketqua:
    print(f"Số: {so}, Vị trí: {vi_tri}")