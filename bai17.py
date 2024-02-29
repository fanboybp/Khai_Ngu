#chen so
 # Chèn số vào đầu danh sách
mlist=[1,3,5,7,8,-2,4,71,2,9,92,92,71,-8,-9,-2,-4,-5]
print("nhap vao so can chen ")
so = int(input("Nhập số : "))
mlist.insert(0, so)
# Chèn số vào cuối danh sách
mlist.append(so)
# Chèn số vào vị trí thứ 5 (index 4) của danh sách
mlist.insert(4, so)
print("in danh sách : ",mlist)
